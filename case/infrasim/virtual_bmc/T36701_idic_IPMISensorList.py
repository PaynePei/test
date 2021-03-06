'''
*********************************************************
Copyright @ 2015 EMC Corporation All Rights Reserved
*********************************************************
'''
from case.CBaseCase import *

class T36701_idic_IPMISensorList(CBaseCase):
    '''
    [Purpose ]: Validate remote sensor command for vBMC
    [Author  ]: Echo.Cheng@emc.com
    [Sprint  ]: Lykan Sprint 25
    [Tickets ]: SST- 629
    '''
    def __init__(self):
        CBaseCase.__init__(self, self.__class__.__name__)
    
    def config(self):
        CBaseCase.config(self)
        # To do: Case specific config
    
    def test(self):
        for obj_rack in self.stack.get_rack_list():
            for obj_node in obj_rack.get_node_list():
                self.log('INFO', 'Check node {} of rack {} ...'.
                         format(obj_node.get_name(), obj_rack.get_name()))
                ret, rsp = obj_node.get_bmc().ipmi.ipmitool_standard_cmd('sensor list')
                self.log('INFO', 'ret: {}'.format(ret))
                self.log('INFO', 'rsp: \n{}'.format(rsp))
                if ret != 0:
                    self.result(FAIL, 'Node {} on rack {} fail to check BMC sensor list, '
                                'ipmitool return: {}, expect: 0, rsp: \n{}'.
                                format(obj_node.get_name(), obj_rack.get_name(), ret, rsp))
    def deconfig(self):
        # To do: Case specific deconfig
        CBaseCase.deconfig(self)
