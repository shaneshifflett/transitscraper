import psycopg2
import csv
import os
from time import time
from datetime import datetime

USERNAME = ''
PASSWORD = ''
HOST = ''
DB = ''
with open('db.cfg', 'rb') as f:
    USERNAME = f.readline().rstrip()
    PASSWORD = f.readline().rstrip()
    HOST = f.readline().rstrip()
    DB = f.readline().rstrip()

path = 'results/'
filenames = os.listdir(path)

routename_ids = {}
vehicleids = {}

insert_eta = "INSERT INTO eta_eta (triptag, direction, seconds, minutes, is_departure, affected_by_layover, route_id, vehicle_id, created, stopid)\
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
insert_eta_route = "INSERT INTO eta_stop_etas (stop_id, eta_id) VALUES(%s, %s)"

def get_route_id(cur, routename):
    get_route = "SELECT id from eta_route where name='%s';"
    try:
        return routename_ids[routename]
    except KeyError:
        try:
            cur.execute(get_route % routename)
            rows = cur.fetchall()
            rowid = rows[0][0]
            routename_ids[routename] = rowid
            return rowid
        except:
            return None

def get_vehicle_id(cur, vehicleid):
    get_vehicle = "SELECT id from eta_vehicle where vehicle_id='%s';"
    try:
        return vehicleids[vehicleid]
    except KeyError:
        try:
            cur.execute(get_vehicle % vehicleid)
            rows = cur.fetchall()
            rowid = rows[0][0]
            vehicleids[vehicleid] = rowid
            return rowid
        except:
            return None

def get_stop_id(cur, stoptag, routeid):
    get_stop = "SELECT id from eta_stop where route_id=%s and tag='%s'"
    try:
        cur.execute(get_stop % (routeid, stoptag))
        rows = cur.fetchall()
        rowid = rows[0][0]
        return rowid
    except:
        return None

try:
    start = datetime.now()
    conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (DB, USERNAME, HOST, PASSWORD))
    cur = conn.cursor()
    for filename in filenames:
        with open(path+filename, 'rb') as f:
            reader = list(csv.reader(f))
            print 'rows=%s' % (len(reader[1:]))
            for idx, row in enumerate(reader[1:]):
                try:
                    routename = row[6]
                    routeid = get_route_id(cur, routename)
                    vehicleid = get_vehicle_id(cur, row[0])
                    stopid = get_stop_id(cur, row[7], routeid)
                    created = datetime.fromtimestamp(float(row[2]))
                    seconds = row[3]
                    is_departure = row[4]
                    dir_tag = row[5]
                    minutes = row[8]
                    affected_by_layover = row[9]
                    triptag = row[1]
                    insert_str = cur.mogrify(insert_eta, (triptag, dir_tag, seconds, minutes, is_departure, affected_by_layover, routeid, vehicleid, created, stopid))
                    eta_id = cur.execute(insert_str)
                    #m2m_str = cur.mogrify(insert_eta_route, (stopid, eta_id))
                    #cur.execute(insert_str)
                    print 'idx=%s time=%s' % (idx, datetime.now())
                except Exception as e:
                    print 'Error inserting eta e=%s' % e
        conn.commit()
        os.system("rm %s" % (path+filename))
        end = datetime.now()
        print 'start=%s end=%s elapsed=%s' % (start, end, start-end)
except Exception as e:
    print 'Exception=%s' %e
