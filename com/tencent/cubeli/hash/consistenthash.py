#!/usr/bin/env python
# encoding=UTF-8
"""
@author jingleyang
@date   2012-06-21
@desc  consistent hashing algorithm
"""
import sys, random, unittest, copy
def serverNodeCmp(na, nb):
    return cmp(na['hashCode'], nb['hashCode'])
class ConsistHash():
    def __init__(self, hashRange=sys.maxint):
        self.cycle = []
        self.maxint = hashRange
    def initHashCycle(self, dataList, vnode=10, weightList=None):
        """
        input:
        dataList [] , objects list ,can be configure ,db conn ...
        vnode      int, number of vnode per each serverNode
        weightList [] , server objects weight
        output:
        isOk    bool
        @desc
            create hash cycle
        """
        dataListLen = len(dataList)
        if 0 == dataListLen:
            print "dataList len must not 0"
            return False
        if None == weightList:
            weightList = [1] * dataListLen
        else:
            if len(weightList) != dataListLen:
                print "weigthList size is diff from dataList size"
                return False
        maxint = self.maxint
        cycle = []
        for i in range(dataListLen):
            totNodeCnt = vnode * weightList[i]
            obj = dataList[i]
            for j in range(totNodeCnt):
                serverNode = {}
                serverNode["hashCode"] = random.randint(0, maxint)
                serverNode["data"] = obj
                cycle.append(serverNode)
        cycle.sort(serverNodeCmp)
        self.cycle = cycle
        print cycle
        return True
    def getHashCycle(self):
        return self.cycle
    def findAimNodeIndexByHash(self, hashCode):
        """
        @desc
            use binary search to find first biger or equal node to hash(key)
            if hash(key) > bigest node , return 0 (first) , this is a cycle
        """
        keyNode = {"hashCode": hashCode}
        cycleLen = len(self.cycle)
        lo = 0
        hi = cycleLen
        while lo < hi:
            mid = (lo + hi) >> 1
            serverNode = self.cycle[mid]
            ret = serverNodeCmp(keyNode, serverNode)
            if ret > 0:
                lo = mid + 1
            elif ret < 0:
                hi = mid
            else:
                lo = mid
                hi = mid
        aimIndex = lo % cycleLen
        return aimIndex
    def findAimNodeIndexByKey(self, key):
        hashCode = hash(key) % self.maxint
        return self.findAimNodeIndexByHash(hashCode)
    def addServerNode(self, obj, vnode=10, weight=1):
        """
            add a serverNode into hashcycle
        """
        serverNode = {
            "hashCode": random.randint(0, self.maxint),
            "data": obj
        }
        totInsertCnt = vnode * weight
        for i in range(totInsertCnt):
            serverNode['hashCode'] = random.randint(0, self.maxint)
            print "serverNode: %s" % (serverNode)
            ind = self.findAimNodeIndexByHash(serverNode['hashCode'])
            print "in addServerNode ind:%d" % (ind)
            if 0 == ind:
                aimNode = self.cycle[ind]
                ret = serverNodeCmp(serverNode, aimNode)
                print "cmp ret:%d" % (ret)
                if ret > 0:
                    ind = len(self.cycle) + 1
                    print "serverNode > cycle[0] so ,ind:%d" % (ind)
            try:
                self.cycle.insert(ind, copy.deepcopy(serverNode))
            except Exception, e:
                return False
        return True
    def rmServerNodeByInd(self, ind):
        try:
            self.cycle.pop(ind)
            return True
        except Exception, e:
            return False
class TestConsistHash(unittest.TestCase):
    def test_usage(self):
        dataList = [
            "127.0.0.1",
            "127.0.0.2",
            "127.0.0.3",
            "127.0.0.4"
        ]
        chashHelper = ConsistHash(100)
        isOk = chashHelper.initHashCycle(dataList, 1, [1, 2, 3, 4])
        self.assertTrue(isOk)
        key = "uin_10000"
        ind = chashHelper.findAimNodeIndexByKey(key)
        node = chashHelper.getHashCycle()[ind]
        hashCode = hash(key) % chashHelper.maxint
        print "key:%s (%d)  insert into node:%s , ind:%d" % (key, hashCode, node, ind)
        print "remove node in ind 0"
        isOk = chashHelper.rmServerNodeByInd(0)
        self.assertTrue(isOk)
        print chashHelper.cycle
        ind = chashHelper.findAimNodeIndexByKey(key)
        node = chashHelper.getHashCycle()[ind]
        print "key:%s (%d)  insert into node:%s , ind:%d" % (key, hashCode, node, ind)
        print "add node 127.0.0.100"
        chashHelper.addServerNode("127.0.0.100", 1, 3)
        print chashHelper.cycle
        ind = chashHelper.findAimNodeIndexByKey(key)
        node = chashHelper.getHashCycle()[ind]
        print "key:%s (%d)  insert into node:%s , ind:%d" % (key, hashCode, node, ind)
if "__main__" == __name__:
    unittest.main(verbosity=3)
