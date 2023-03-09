"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""
from acp_times import open_time, close_time
import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_brevet1():
    start_time = arrow.get("2023-02-22 10:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = {
              0: (start_time, start_time.shift(hours=1)),
             50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3.5)),
            150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10)),
            200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13.5)),
            }

    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close

def test_brevet2():
    start_time = arrow.get("2023-02-22 00:00", "YYYY-MM-DD HH:mm")
    dist = 300
    checkpoints = {
              0: (start_time, start_time.shift(hours=1)),
             15: (start_time.shift(minutes=26), start_time.shift(hours=1, minutes=45)),
             60: (start_time.shift(hours=1, minutes=46), start_time.shift(hours=4)),           
            150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10)),
            220: (start_time.shift(hours=6, minutes=30), start_time.shift(hours=14, minutes=40)),
            360: (start_time.shift(hours=9), start_time.shift(hours=20)),            
            }

    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close

def test_brevet3():
    start_time = arrow.get("2023-02-22 12:30", "YYYY-MM-DD HH:mm")
    dist = 600
    checkpoints = {
              0: (start_time, start_time.shift(hours=1)),
            100: (start_time.shift(hours=2, minutes=56), start_time.shift(hours=6, minutes=40)),
            250: (start_time.shift(hours=7, minutes=27), start_time.shift(hours=16, minutes=40)),
            400: (start_time.shift(hours=12, minutes=8), start_time.shift(days=1, hours=2, minutes=40)),
            550: (start_time.shift(hours=17, minutes=8), start_time.shift(days=1, hours=12, minutes=40)),
            620: (start_time.shift(hours=18, minutes=48), start_time.shift(days=1, hours=16)),            
            }

    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close

def test_brevet4():
    start_time = arrow.get("2023-02-22 04:56", "YYYY-MM-DD HH:mm")
    dist = 1000
    checkpoints = {
              0: (start_time, start_time.shift(hours=1)),
            200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=20)),
            335: (start_time.shift(hours=10, minutes=6), start_time.shift(hours=22, minutes=20)),
            568: (start_time.shift(hours=17, minutes=44), start_time.shift(days=1, hours=13, minutes=52)),
            800: (start_time.shift(days=1, hours=1, minutes=57), start_time.shift(days=2, hours=9.5)),
           1200: (start_time.shift(days=1, hours=9, minutes=5), start_time.shift(days=3, hours=3)),            
            }

    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close

def test_brevet5():
    start_time = arrow.get("2023-02-22 07:23", "YYYY-MM-DD HH:mm")
    dist = 400
    checkpoints = {
              0: (start_time, start_time.shift(hours=1)),
             13: (start_time.shift(minutes=23), start_time.shift(hours=1, minutes=39)),
             53: (start_time.shift(hours=1, minutes=34), start_time.shift(hours=3, minutes=39)),
            100: (start_time.shift(hours=2, minutes=56), start_time.shift(hours=6, minutes=40)),
            267: (start_time.shift(hours=7, minutes=59), start_time.shift(hours=17, minutes=48)),
            344: (start_time.shift(hours=10, minutes=23), start_time.shift(hours=22, minutes=56)),
            400: (start_time.shift(hours=12, minutes=8), start_time.shift(days=1, hours=3)),            
            }

    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close
