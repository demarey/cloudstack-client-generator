from BaseCloudStackClient import BaseCloudStackClient


class CloudStackClient(BaseCloudStackClient.BaseCloudStackClient):

    def createRemoteAccessVpn(self, publicIpId, account = "", domainId = "", ipRange = "", openFirewall = ""):
        '''
        Creates a l2tp/ipsec remote access vpn
        '''

        return self.request("createRemoteAccessVpn", {
            'publicipid' : publicIpId,
            'account' : account,
            'domainid' : domainId,
            'iprange' : ipRange,
            'openfirewall' : openFirewall,
        })
    
    def deleteRemoteAccessVpn(self, publicIpId):
        '''
        Destroys a l2tp/ipsec remote access vpn
        '''

        return self.request("deleteRemoteAccessVpn", {
            'publicipid' : publicIpId,
        })
    
    def listRemoteAccessVpns(self, publicIpId, account = "", domainId = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = ""):
        '''
        Lists remote access vpns
        '''

        return self.request("listRemoteAccessVpns", {
            'publicipid' : publicIpId,
            'account' : account,
            'domainid' : domainId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
        })
    
    def createVpnCustomerGateway(self, cidrList, espPolicy, gateway, ikePolicy, ipsecPsk, account = "", domainId = "", dpd = "", espLifeTime = "", ikeLifeTime = "", name = ""):
        '''
        Creates site to site vpn customer gateway
        '''

        return self.request("createVpnCustomerGateway", {
            'cidrlist' : cidrList,
            'esppolicy' : espPolicy,
            'gateway' : gateway,
            'ikepolicy' : ikePolicy,
            'ipsecpsk' : ipsecPsk,
            'account' : account,
            'domainid' : domainId,
            'dpd' : dpd,
            'esplifetime' : espLifeTime,
            'ikelifetime' : ikeLifeTime,
            'name' : name,
        })
    
    def createVpnGateway(self, vpcId):
        '''
        Creates site to site vpn local gateway
        '''

        return self.request("createVpnGateway", {
            'vpcid' : vpcId,
        })
    
    def createVpnConnection(self, s2sCustomerGatewayId, s2sVpnGatewayId):
        '''
        Create site to site vpn connection
        '''

        return self.request("createVpnConnection", {
            's2scustomergatewayid' : s2sCustomerGatewayId,
            's2svpngatewayid' : s2sVpnGatewayId,
        })
    
    def deleteVpnCustomerGateway(self, id):
        '''
        Delete site to site vpn customer gateway
        '''

        return self.request("deleteVpnCustomerGateway", {
            'id' : id,
        })
    
    def deleteVpnGateway(self, id):
        '''
        Delete site to site vpn gateway
        '''

        return self.request("deleteVpnGateway", {
            'id' : id,
        })
    
    def deleteVpnConnection(self, id):
        '''
        Delete site to site vpn connection
        '''

        return self.request("deleteVpnConnection", {
            'id' : id,
        })
    
    def updateVpnCustomerGateway(self, id, cidrList, espPolicy, gateway, ikePolicy, ipsecPsk, account = "", domainId = "", dpd = "", espLifeTime = "", ikeLifeTime = "", name = ""):
        '''
        Update site to site vpn customer gateway
        '''

        return self.request("updateVpnCustomerGateway", {
            'id' : id,
            'cidrlist' : cidrList,
            'esppolicy' : espPolicy,
            'gateway' : gateway,
            'ikepolicy' : ikePolicy,
            'ipsecpsk' : ipsecPsk,
            'account' : account,
            'domainid' : domainId,
            'dpd' : dpd,
            'esplifetime' : espLifeTime,
            'ikelifetime' : ikeLifeTime,
            'name' : name,
        })
    
    def resetVpnConnection(self, id, account = "", domainId = ""):
        '''
        Reset site to site vpn connection
        '''

        return self.request("resetVpnConnection", {
            'id' : id,
            'account' : account,
            'domainid' : domainId,
        })
    
    def listVpnCustomerGateways(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = ""):
        '''
        Lists site to site vpn customer gateways
        '''

        return self.request("listVpnCustomerGateways", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
        })
    
    def listVpnGateways(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", vpcId = ""):
        '''
        Lists site 2 site vpn gateways
        '''

        return self.request("listVpnGateways", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'vpcid' : vpcId,
        })
    
    def listVpnConnections(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", vpcId = ""):
        '''
        Lists site to site vpn connection gateways
        '''

        return self.request("listVpnConnections", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'vpcid' : vpcId,
        })
    
    def deployVirtualMachine(self, serviceOfferingId, templateId, zoneId, account = "", diskOfferingId = "", displayName = "", domainId = "", group = "", hostId = "", hypervisor = "", ipAddress = "", ipToNetWorkList = "", keyboard = "", keyPair = "", name = "", networkIds = "", projectId = "", securityGroupIds = "", securityGroupNames = "", size = "", startVm = "", userData = ""):
        '''
        Creates and automatically starts a virtual machine based on a service offering, disk offering, and template.
        '''

        return self.request("deployVirtualMachine", {
            'serviceofferingid' : serviceOfferingId,
            'templateid' : templateId,
            'zoneid' : zoneId,
            'account' : account,
            'diskofferingid' : diskOfferingId,
            'displayname' : displayName,
            'domainid' : domainId,
            'group' : group,
            'hostid' : hostId,
            'hypervisor' : hypervisor,
            'ipaddress' : ipAddress,
            'iptonetworklist' : ipToNetWorkList,
            'keyboard' : keyboard,
            'keypair' : keyPair,
            'name' : name,
            'networkids' : networkIds,
            'projectid' : projectId,
            'securitygroupids' : securityGroupIds,
            'securitygroupnames' : securityGroupNames,
            'size' : size,
            'startvm' : startVm,
            'userdata' : userData,
        })
    
    def destroyVirtualMachine(self, id):
        '''
        Destroys a virtual machine. Once destroyed, only the administrator can recover it.
        '''

        return self.request("destroyVirtualMachine", {
            'id' : id,
        })
    
    def rebootVirtualMachine(self, id):
        '''
        Reboots a virtual machine.
        '''

        return self.request("rebootVirtualMachine", {
            'id' : id,
        })
    
    def startVirtualMachine(self, id, hostId = ""):
        '''
        Starts a virtual machine.
        '''

        return self.request("startVirtualMachine", {
            'id' : id,
            'hostid' : hostId,
        })
    
    def stopVirtualMachine(self, id, forced = ""):
        '''
        Stops a virtual machine.
        '''

        return self.request("stopVirtualMachine", {
            'id' : id,
            'forced' : forced,
        })
    
    def resetPasswordForVirtualMachine(self, id):
        '''
        Resets the password for virtual machine. The virtual machine must be in a "Stopped" state and the template must already support this feature for this command to take effect. [async]
        '''

        return self.request("resetPasswordForVirtualMachine", {
            'id' : id,
        })
    
    def changeServiceForVirtualMachine(self, id, serviceOfferingId):
        '''
        Changes the service offering for a virtual machine. The virtual machine must be in a "Stopped" state for this command to take effect.
        '''

        return self.request("changeServiceForVirtualMachine", {
            'id' : id,
            'serviceofferingid' : serviceOfferingId,
        })
    
    def updateVirtualMachine(self, id, displayName = "", group = "", haEnable = "", osTypeId = "", userData = ""):
        '''
        Updates properties of a virtual machine. The VM has to be stopped and restarted for the new properties to take effect. UpdateVirtualMachine does not first check whether the VM is stopped. Therefore, stop the VM manually before issuing this call.
        '''

        return self.request("updateVirtualMachine", {
            'id' : id,
            'displayname' : displayName,
            'group' : group,
            'haenable' : haEnable,
            'ostypeid' : osTypeId,
            'userdata' : userData,
        })
    
    def recoverVirtualMachine(self, id):
        '''
        Recovers a virtual machine.
        '''

        return self.request("recoverVirtualMachine", {
            'id' : id,
        })
    
    def listVirtualMachines(self, account = "", details = "", domainId = "", forVirtualNetwork = "", groupId = "", hostId = "", hypervisor = "", id = "", isoId = "", isRecursive = "", keyword = "", listAll = "", name = "", networkId = "", page = "", pageSize = "", podId = "", projectId = "", state = "", storageId = "", tags = "", templateId = "", vpcId = "", zoneId = ""):
        '''
        List the virtual machines owned by the account.
        '''

        return self.request("listVirtualMachines", {
            'account' : account,
            'details' : details,
            'domainid' : domainId,
            'forvirtualnetwork' : forVirtualNetwork,
            'groupid' : groupId,
            'hostid' : hostId,
            'hypervisor' : hypervisor,
            'id' : id,
            'isoid' : isoId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'podid' : podId,
            'projectid' : projectId,
            'state' : state,
            'storageid' : storageId,
            'tags' : tags,
            'templateid' : templateId,
            'vpcid' : vpcId,
            'zoneid' : zoneId,
        })
    
    def getVMPassword(self, id):
        '''
        Returns an encrypted password for the VM
        '''

        return self.request("getVMPassword", {
            'id' : id,
        })
    
    def restoreVirtualMachine(self, virtualMachineId):
        '''
        Restore a VM to original template or specific snapshot
        '''

        return self.request("restoreVirtualMachine", {
            'virtualmachineid' : virtualMachineId,
        })
    
    def createVPC(self, cidr, displayText, name, vpcOfferingId, zoneId, account = "", domainId = "", networkDomain = "", projectId = ""):
        '''
        Creates a VPC
        '''

        return self.request("createVPC", {
            'cidr' : cidr,
            'displaytext' : displayText,
            'name' : name,
            'vpcofferingid' : vpcOfferingId,
            'zoneid' : zoneId,
            'account' : account,
            'domainid' : domainId,
            'networkdomain' : networkDomain,
            'projectid' : projectId,
        })
    
    def listVPCs(self, account = "", account = "", cidr = "", displayText = "", domainId = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = "", restartRequired = "", state = "", supportedServices = "", tags = "", vpcOfferingId = "", zoneId = ""):
        '''
        Lists VPCs
        '''

        return self.request("listVPCs", {
            'account' : account,
            'account' : account,
            'cidr' : cidr,
            'displaytext' : displayText,
            'domainid' : domainId,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'restartrequired' : restartRequired,
            'state' : state,
            'supportedservices' : supportedServices,
            'tags' : tags,
            'vpcofferingid' : vpcOfferingId,
            'zoneid' : zoneId,
        })
    
    def deleteVPC(self, id):
        '''
        Deletes a VPC
        '''

        return self.request("deleteVPC", {
            'id' : id,
        })
    
    def updateVPC(self, displayText = "", id = "", name = ""):
        '''
        Updates a VPC
        '''

        return self.request("updateVPC", {
            'displaytext' : displayText,
            'id' : id,
            'name' : name,
        })
    
    def restartVPC(self, id = ""):
        '''
        Restarts a VPC
        '''

        return self.request("restartVPC", {
            'id' : id,
        })
    
    def listVPCOfferings(self, displayText = "", id = "", isDefault = "", keyword = "", name = "", page = "", pageSize = "", state = "", supportedServices = ""):
        '''
        Lists VPC offerings
        '''

        return self.request("listVPCOfferings", {
            'displaytext' : displayText,
            'id' : id,
            'isdefault' : isDefault,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'state' : state,
            'supportedservices' : supportedServices,
        })
    
    def listPrivateGateways(self, account = "", domainId = "", id = "", ipAddress = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", state = "", vlan = "", vpcId = ""):
        '''
        List private gateways
        '''

        return self.request("listPrivateGateways", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'ipaddress' : ipAddress,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'state' : state,
            'vlan' : vlan,
            'vpcid' : vpcId,
        })
    
    def createStaticRoute(self, cidr, gatewayId):
        '''
        Creates a static route
        '''

        return self.request("createStaticRoute", {
            'cidr' : cidr,
            'gatewayid' : gatewayId,
        })
    
    def deleteStaticRoute(self, id):
        '''
        Deletes a static route
        '''

        return self.request("deleteStaticRoute", {
            'id' : id,
        })
    
    def listStaticRoutes(self, account = "", domainId = "", gatewayId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", tags = "", vpcId = ""):
        '''
        Lists all static routes
        '''

        return self.request("listStaticRoutes", {
            'account' : account,
            'domainid' : domainId,
            'gatewayid' : gatewayId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'tags' : tags,
            'vpcid' : vpcId,
        })
    
    def createLoadBalancerRule(self, algorithm, name, privatePort, publicPort, account = "", cidrList = "", description = "", domainId = "", networkId = "", openFirewall = "", publicIpId = "", zoneId = ""):
        '''
        Creates a load balancer rule
        '''

        return self.request("createLoadBalancerRule", {
            'algorithm' : algorithm,
            'name' : name,
            'privateport' : privatePort,
            'publicport' : publicPort,
            'account' : account,
            'cidrlist' : cidrList,
            'description' : description,
            'domainid' : domainId,
            'networkid' : networkId,
            'openfirewall' : openFirewall,
            'publicipid' : publicIpId,
            'zoneid' : zoneId,
        })
    
    def deleteLoadBalancerRule(self, id):
        '''
        Deletes a load balancer rule.
        '''

        return self.request("deleteLoadBalancerRule", {
            'id' : id,
        })
    
    def removeFromLoadBalancerRule(self, id, virtualMachineIds):
        '''
        Removes a virtual machine or a list of virtual machines from a load balancer rule.
        '''

        return self.request("removeFromLoadBalancerRule", {
            'id' : id,
            'virtualmachineids' : virtualMachineIds,
        })
    
    def assignToLoadBalancerRule(self, id, virtualMachineIds):
        '''
        Assigns virtual machine or a list of virtual machines to a load balancer rule.
        '''

        return self.request("assignToLoadBalancerRule", {
            'id' : id,
            'virtualmachineids' : virtualMachineIds,
        })
    
    def createLBStickinessPolicy(self, lbruleId, methodName, name, description = "", param = ""):
        '''
        Creates a Load Balancer stickiness policy
        '''

        return self.request("createLBStickinessPolicy", {
            'lbruleid' : lbruleId,
            'methodname' : methodName,
            'name' : name,
            'description' : description,
            'param' : param,
        })
    
    def deleteLBStickinessPolicy(self, id):
        '''
        Deletes a LB stickiness policy.
        '''

        return self.request("deleteLBStickinessPolicy", {
            'id' : id,
        })
    
    def listLoadBalancerRules(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = "", publicIpId = "", tags = "", virtualMachineId = "", zoneId = ""):
        '''
        Lists load balancer rules.
        '''

        return self.request("listLoadBalancerRules", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'publicipid' : publicIpId,
            'tags' : tags,
            'virtualmachineid' : virtualMachineId,
            'zoneid' : zoneId,
        })
    
    def listLBStickinessPolicies(self, lbruleId, keyword = "", page = "", pageSize = ""):
        '''
        Lists LBStickiness policies.
        '''

        return self.request("listLBStickinessPolicies", {
            'lbruleid' : lbruleId,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listLoadBalancerRuleInstances(self, id, applied = "", keyword = "", page = "", pageSize = ""):
        '''
        List all virtual machine instances that are assigned to a load balancer rule.
        '''

        return self.request("listLoadBalancerRuleInstances", {
            'id' : id,
            'applied' : applied,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def updateLoadBalancerRule(self, id, algorithm = "", description = "", name = ""):
        '''
        Updates load balancer
        '''

        return self.request("updateLoadBalancerRule", {
            'id' : id,
            'algorithm' : algorithm,
            'description' : description,
            'name' : name,
        })
    
    def startRouter(self, id):
        '''
        Starts a router.
        '''

        return self.request("startRouter", {
            'id' : id,
        })
    
    def rebootRouter(self, id):
        '''
        Starts a router.
        '''

        return self.request("rebootRouter", {
            'id' : id,
        })
    
    def stopRouter(self, id, forced = ""):
        '''
        Stops a router.
        '''

        return self.request("stopRouter", {
            'id' : id,
            'forced' : forced,
        })
    
    def destroyRouter(self, id):
        '''
        Destroys a router.
        '''

        return self.request("destroyRouter", {
            'id' : id,
        })
    
    def changeServiceForRouter(self, id, serviceOfferingId):
        '''
        Upgrades domain router to a new service offering
        '''

        return self.request("changeServiceForRouter", {
            'id' : id,
            'serviceofferingid' : serviceOfferingId,
        })
    
    def listRouters(self, account = "", domainId = "", forVpc = "", hostId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", networkId = "", page = "", pageSize = "", podId = "", projectId = "", state = "", vpcId = "", zoneId = ""):
        '''
        List routers.
        '''

        return self.request("listRouters", {
            'account' : account,
            'domainid' : domainId,
            'forvpc' : forVpc,
            'hostid' : hostId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'podid' : podId,
            'projectid' : projectId,
            'state' : state,
            'vpcid' : vpcId,
            'zoneid' : zoneId,
        })
    
    def createVirtualRouterElement(self, nspId):
        '''
        Create a virtual router element.
        '''

        return self.request("createVirtualRouterElement", {
            'nspid' : nspId,
        })
    
    def configureVirtualRouterElement(self, id, enabled):
        '''
        Configures a virtual router element.
        '''

        return self.request("configureVirtualRouterElement", {
            'id' : id,
            'enabled' : enabled,
        })
    
    def listVirtualRouterElements(self, enabled = "", id = "", keyword = "", nspId = "", page = "", pageSize = ""):
        '''
        Lists all available virtual router elements.
        '''

        return self.request("listVirtualRouterElements", {
            'enabled' : enabled,
            'id' : id,
            'keyword' : keyword,
            'nspid' : nspId,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def createProject(self, displayText, name, account = "", domainId = ""):
        '''
        Creates a project
        '''

        return self.request("createProject", {
            'displaytext' : displayText,
            'name' : name,
            'account' : account,
            'domainid' : domainId,
        })
    
    def deleteProject(self, id):
        '''
        Deletes a project
        '''

        return self.request("deleteProject", {
            'id' : id,
        })
    
    def updateProject(self, id, account = "", displayText = ""):
        '''
        Updates a project
        '''

        return self.request("updateProject", {
            'id' : id,
            'account' : account,
            'displaytext' : displayText,
        })
    
    def activateProject(self, id):
        '''
        Activates a project
        '''

        return self.request("activateProject", {
            'id' : id,
        })
    
    def suspendProject(self, id):
        '''
        Suspends a project
        '''

        return self.request("suspendProject", {
            'id' : id,
        })
    
    def listProjects(self, account = "", displayText = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", state = "", tags = ""):
        '''
        Lists projects and provides detailed information for listed projects
        '''

        return self.request("listProjects", {
            'account' : account,
            'displaytext' : displayText,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'state' : state,
            'tags' : tags,
        })
    
    def listProjectInvitations(self, account = "", activeOnly = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", state = ""):
        '''
        Lists projects and provides detailed information for listed projects
        '''

        return self.request("listProjectInvitations", {
            'account' : account,
            'activeonly' : activeOnly,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'state' : state,
        })
    
    def updateProjectInvitation(self, projectId, accept = "", account = "", token = ""):
        '''
        Accepts or declines project invitation
        '''

        return self.request("updateProjectInvitation", {
            'projectid' : projectId,
            'accept' : accept,
            'account' : account,
            'token' : token,
        })
    
    def deleteProjectInvitation(self, id):
        '''
        Accepts or declines project invitation
        '''

        return self.request("deleteProjectInvitation", {
            'id' : id,
        })
    
    def listNetworkOfferings(self, availability = "", displayText = "", forVpc = "", guestIpType = "", id = "", isDefault = "", isTagged = "", keyword = "", name = "", networkId = "", page = "", pageSize = "", sourceNatSupported = "", specifyIpRanges = "", specifyVlan = "", state = "", supportedServices = "", tags = "", trafficType = "", zoneId = ""):
        '''
        Lists all available network offerings.
        '''

        return self.request("listNetworkOfferings", {
            'availability' : availability,
            'displaytext' : displayText,
            'forvpc' : forVpc,
            'guestiptype' : guestIpType,
            'id' : id,
            'isdefault' : isDefault,
            'istagged' : isTagged,
            'keyword' : keyword,
            'name' : name,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'sourcenatsupported' : sourceNatSupported,
            'specifyipranges' : specifyIpRanges,
            'specifyvlan' : specifyVlan,
            'state' : state,
            'supportedservices' : supportedServices,
            'tags' : tags,
            'traffictype' : trafficType,
            'zoneid' : zoneId,
        })
    
    def createNetwork(self, displayText, name, networkOfferingId, zoneId, account = "", aclType = "", domainId = "", endIp = "", gateway = "", netmask = "", networkDomain = "", physicalNetworkId = "", projectId = "", startIp = "", subDomainAccess = "", vlan = "", vpcId = ""):
        '''
        Creates a network
        '''

        return self.request("createNetwork", {
            'displaytext' : displayText,
            'name' : name,
            'networkofferingid' : networkOfferingId,
            'zoneid' : zoneId,
            'account' : account,
            'acltype' : aclType,
            'domainid' : domainId,
            'endip' : endIp,
            'gateway' : gateway,
            'netmask' : netmask,
            'networkdomain' : networkDomain,
            'physicalnetworkid' : physicalNetworkId,
            'projectid' : projectId,
            'startip' : startIp,
            'subdomainaccess' : subDomainAccess,
            'vlan' : vlan,
            'vpcid' : vpcId,
        })
    
    def deleteNetwork(self, id):
        '''
        Deletes a network
        '''

        return self.request("deleteNetwork", {
            'id' : id,
        })
    
    def listNetworks(self, account = "", aclType = "", canUseForDeploy = "", domainId = "", forVpc = "", id = "", isRecursive = "", isSystem = "", keyword = "", listAll = "", page = "", pageSize = "", physicalNetworkId = "", projectId = "", restartRequired = "", specifyIpRanges = "", supportedServices = "", tags = "", trafficType = "", type = "", vpcId = "", zoneId = ""):
        '''
        Lists all available networks.
        '''

        return self.request("listNetworks", {
            'account' : account,
            'acltype' : aclType,
            'canusefordeploy' : canUseForDeploy,
            'domainid' : domainId,
            'forvpc' : forVpc,
            'id' : id,
            'isrecursive' : isRecursive,
            'issystem' : isSystem,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'physicalnetworkid' : physicalNetworkId,
            'projectid' : projectId,
            'restartrequired' : restartRequired,
            'specifyipranges' : specifyIpRanges,
            'supportedservices' : supportedServices,
            'tags' : tags,
            'traffictype' : trafficType,
            'type' : type,
            'vpcid' : vpcId,
            'zoneid' : zoneId,
        })
    
    def restartNetwork(self, id, cleanup = ""):
        '''
        Restarts the network; includes 1) restarting network elements - virtual routers, dhcp servers 2) reapplying all public ips 3) reapplying loadBalancing/portForwarding rules
        '''

        return self.request("restartNetwork", {
            'id' : id,
            'cleanup' : cleanup,
        })
    
    def updateNetwork(self, id, changeCidr = "", displayText = "", name = "", networkDomain = "", networkOfferingId = ""):
        '''
        Updates a network
        '''

        return self.request("updateNetwork", {
            'id' : id,
            'changecidr' : changeCidr,
            'displaytext' : displayText,
            'name' : name,
            'networkdomain' : networkDomain,
            'networkofferingid' : networkOfferingId,
        })
    
    def createNetworkACL(self, networkId, protocol, cidrList = "", endPort = "", icmpCode = "", icmpType = "", startPort = "", trafficType = ""):
        '''
        Creates a ACL rule the given network (the network has to belong to VPC)
        '''

        return self.request("createNetworkACL", {
            'networkid' : networkId,
            'protocol' : protocol,
            'cidrlist' : cidrList,
            'endport' : endPort,
            'icmpcode' : icmpCode,
            'icmptype' : icmpType,
            'startport' : startPort,
            'traffictype' : trafficType,
        })
    
    def deleteNetworkACL(self, id):
        '''
        Deletes a Network ACL
        '''

        return self.request("deleteNetworkACL", {
            'id' : id,
        })
    
    def listNetworkACLs(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", networkId = "", page = "", pageSize = "", projectId = "", tags = "", trafficType = ""):
        '''
        Lists all network ACLs
        '''

        return self.request("listNetworkACLs", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'tags' : tags,
            'traffictype' : trafficType,
        })
    
    def attachIso(self, id, virtualMachineId):
        '''
        Attaches an ISO to a virtual machine.
        '''

        return self.request("attachIso", {
            'id' : id,
            'virtualmachineid' : virtualMachineId,
        })
    
    def detachIso(self, virtualMachineId):
        '''
        Detaches any ISO file (if any) currently attached to a virtual machine.
        '''

        return self.request("detachIso", {
            'virtualmachineid' : virtualMachineId,
        })
    
    def listIsos(self, account = "", bootable = "", domainId = "", hypervisor = "", id = "", isoFilter = "", isPublic = "", isReady = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = "", tags = "", zoneId = ""):
        '''
        Lists all available ISO files.
        '''

        return self.request("listIsos", {
            'account' : account,
            'bootable' : bootable,
            'domainid' : domainId,
            'hypervisor' : hypervisor,
            'id' : id,
            'isofilter' : isoFilter,
            'ispublic' : isPublic,
            'isready' : isReady,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'tags' : tags,
            'zoneid' : zoneId,
        })
    
    def updateIso(self, id, bootable = "", displayText = "", format = "", name = "", osTypeId = "", passwordEnabled = "", sortKey = ""):
        '''
        Updates an ISO file.
        '''

        return self.request("updateIso", {
            'id' : id,
            'bootable' : bootable,
            'displaytext' : displayText,
            'format' : format,
            'name' : name,
            'ostypeid' : osTypeId,
            'passwordenabled' : passwordEnabled,
            'sortkey' : sortKey,
        })
    
    def deleteIso(self, id, zoneId = ""):
        '''
        Deletes an ISO file.
        '''

        return self.request("deleteIso", {
            'id' : id,
            'zoneid' : zoneId,
        })
    
    def copyIso(self, id, destzoneId, sourceZoneId):
        '''
        Copies a template from one zone to another.
        '''

        return self.request("copyIso", {
            'id' : id,
            'destzoneid' : destzoneId,
            'sourcezoneid' : sourceZoneId,
        })
    
    def updateIsoPermissions(self, id, accounts = "", isExtractable = "", isFeatured = "", isPublic = "", op = "", projectids = ""):
        '''
        Updates iso permissions
        '''

        return self.request("updateIsoPermissions", {
            'id' : id,
            'accounts' : accounts,
            'isextractable' : isExtractable,
            'isfeatured' : isFeatured,
            'ispublic' : isPublic,
            'op' : op,
            'projectids' : projectids,
        })
    
    def listIsoPermissions(self, id):
        '''
        List template visibility and all accounts that have permissions to view this template.
        '''

        return self.request("listIsoPermissions", {
            'id' : id,
        })
    
    def extractIso(self, id, mode, url = "", zoneId = ""):
        '''
        Extracts an ISO
        '''

        return self.request("extractIso", {
            'id' : id,
            'mode' : mode,
            'url' : url,
            'zoneid' : zoneId,
        })
    
    def attachVolume(self, id, virtualMachineId, deviceId = ""):
        '''
        Attaches a disk volume to a virtual machine.
        '''

        return self.request("attachVolume", {
            'id' : id,
            'virtualmachineid' : virtualMachineId,
            'deviceid' : deviceId,
        })
    
    def uploadVolume(self, format, name, url, zoneId, account = "", checksum = "", domainId = ""):
        '''
        Uploads a data disk.
        '''

        return self.request("uploadVolume", {
            'format' : format,
            'name' : name,
            'url' : url,
            'zoneid' : zoneId,
            'account' : account,
            'checksum' : checksum,
            'domainid' : domainId,
        })
    
    def detachVolume(self, deviceId = "", id = "", virtualMachineId = ""):
        '''
        Detaches a disk volume from a virtual machine.
        '''

        return self.request("detachVolume", {
            'deviceid' : deviceId,
            'id' : id,
            'virtualmachineid' : virtualMachineId,
        })
    
    def createVolume(self, name, account = "", diskOfferingId = "", domainId = "", projectId = "", size = "", snapshotId = "", zoneId = ""):
        '''
        Creates a disk volume from a disk offering. This disk volume must still be attached to a virtual machine to make use of it.
        '''

        return self.request("createVolume", {
            'name' : name,
            'account' : account,
            'diskofferingid' : diskOfferingId,
            'domainid' : domainId,
            'projectid' : projectId,
            'size' : size,
            'snapshotid' : snapshotId,
            'zoneid' : zoneId,
        })
    
    def deleteVolume(self, id):
        '''
        Deletes a detached disk volume.
        '''

        return self.request("deleteVolume", {
            'id' : id,
        })
    
    def listVolumes(self, account = "", domainId = "", hostId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", podId = "", projectId = "", tags = "", type = "", virtualMachineId = "", zoneId = ""):
        '''
        Lists all volumes.
        '''

        return self.request("listVolumes", {
            'account' : account,
            'domainid' : domainId,
            'hostid' : hostId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'podid' : podId,
            'projectid' : projectId,
            'tags' : tags,
            'type' : type,
            'virtualmachineid' : virtualMachineId,
            'zoneid' : zoneId,
        })
    
    def extractVolume(self, id, mode, zoneId, url = ""):
        '''
        Extracts volume
        '''

        return self.request("extractVolume", {
            'id' : id,
            'mode' : mode,
            'zoneid' : zoneId,
            'url' : url,
        })
    
    def migrateVolume(self, storageId, volumeId):
        '''
        Migrate volume
        '''

        return self.request("migrateVolume", {
            'storageid' : storageId,
            'volumeid' : volumeId,
        })
    
    def createTemplate(self, displayText, name, osTypeId, bits = "", details = "", isFeatured = "", isPublic = "", passwordEnabled = "", requireShvm = "", snapshotId = "", templateTag = "", url = "", virtualMachineId = "", volumeId = ""):
        '''
        Creates a template of a virtual machine. The virtual machine must be in a STOPPED state. A template created from this command is automatically designated as a private template visible to the account that created it.
        '''

        return self.request("createTemplate", {
            'displaytext' : displayText,
            'name' : name,
            'ostypeid' : osTypeId,
            'bits' : bits,
            'details' : details,
            'isfeatured' : isFeatured,
            'ispublic' : isPublic,
            'passwordenabled' : passwordEnabled,
            'requireshvm' : requireShvm,
            'snapshotid' : snapshotId,
            'templatetag' : templateTag,
            'url' : url,
            'virtualmachineid' : virtualMachineId,
            'volumeid' : volumeId,
        })
    
    def updateTemplate(self, id, bootable = "", displayText = "", format = "", name = "", osTypeId = "", passwordEnabled = "", sortKey = ""):
        '''
        Updates attributes of a template.
        '''

        return self.request("updateTemplate", {
            'id' : id,
            'bootable' : bootable,
            'displaytext' : displayText,
            'format' : format,
            'name' : name,
            'ostypeid' : osTypeId,
            'passwordenabled' : passwordEnabled,
            'sortkey' : sortKey,
        })
    
    def copyTemplate(self, id, destzoneId, sourceZoneId):
        '''
        Copies a template from one zone to another.
        '''

        return self.request("copyTemplate", {
            'id' : id,
            'destzoneid' : destzoneId,
            'sourcezoneid' : sourceZoneId,
        })
    
    def deleteTemplate(self, id, zoneId = ""):
        '''
        Deletes a template from the system. All virtual machines using the deleted template will not be affected.
        '''

        return self.request("deleteTemplate", {
            'id' : id,
            'zoneid' : zoneId,
        })
    
    def listTemplates(self, templateFilter, account = "", domainId = "", hypervisor = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = "", tags = "", zoneId = ""):
        '''
        List all public, private, and privileged templates.
        '''

        return self.request("listTemplates", {
            'templatefilter' : templateFilter,
            'account' : account,
            'domainid' : domainId,
            'hypervisor' : hypervisor,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'tags' : tags,
            'zoneid' : zoneId,
        })
    
    def updateTemplatePermissions(self, id, accounts = "", isExtractable = "", isFeatured = "", isPublic = "", op = "", projectids = ""):
        '''
        Updates a template visibility permissions. A public template is visible to all accounts within the same domain. A private template is visible only to the owner of the template. A priviledged template is a private template with account permissions added. Only accounts specified under the template permissions are visible to them.
        '''

        return self.request("updateTemplatePermissions", {
            'id' : id,
            'accounts' : accounts,
            'isextractable' : isExtractable,
            'isfeatured' : isFeatured,
            'ispublic' : isPublic,
            'op' : op,
            'projectids' : projectids,
        })
    
    def listTemplatePermissions(self, id):
        '''
        List template visibility and all accounts that have permissions to view this template.
        '''

        return self.request("listTemplatePermissions", {
            'id' : id,
        })
    
    def extractTemplate(self, id, mode, url = "", zoneId = ""):
        '''
        Extracts a template
        '''

        return self.request("extractTemplate", {
            'id' : id,
            'mode' : mode,
            'url' : url,
            'zoneid' : zoneId,
        })
    
    def createSecurityGroup(self, name, account = "", description = "", domainId = "", projectId = ""):
        '''
        Creates a security group
        '''

        return self.request("createSecurityGroup", {
            'name' : name,
            'account' : account,
            'description' : description,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def deleteSecurityGroup(self, account = "", domainId = "", id = "", name = "", projectId = ""):
        '''
        Deletes security group
        '''

        return self.request("deleteSecurityGroup", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'name' : name,
            'projectid' : projectId,
        })
    
    def authorizeSecurityGroupIngress(self, account = "", cidrList = "", domainId = "", endPort = "", icmpCode = "", icmpType = "", projectId = "", protocol = "", securityGroupId = "", securityGroupName = "", startPort = "", userSecurityGroupList = ""):
        '''
        Authorizes a particular ingress rule for this security group
        '''

        return self.request("authorizeSecurityGroupIngress", {
            'account' : account,
            'cidrlist' : cidrList,
            'domainid' : domainId,
            'endport' : endPort,
            'icmpcode' : icmpCode,
            'icmptype' : icmpType,
            'projectid' : projectId,
            'protocol' : protocol,
            'securitygroupid' : securityGroupId,
            'securitygroupname' : securityGroupName,
            'startport' : startPort,
            'usersecuritygrouplist' : userSecurityGroupList,
        })
    
    def revokeSecurityGroupIngress(self, id):
        '''
        Deletes a particular ingress rule from this security group
        '''

        return self.request("revokeSecurityGroupIngress", {
            'id' : id,
        })
    
    def authorizeSecurityGroupEgress(self, account = "", cidrList = "", domainId = "", endPort = "", icmpCode = "", icmpType = "", projectId = "", protocol = "", securityGroupId = "", securityGroupName = "", startPort = "", userSecurityGroupList = ""):
        '''
        Authorizes a particular egress rule for this security group
        '''

        return self.request("authorizeSecurityGroupEgress", {
            'account' : account,
            'cidrlist' : cidrList,
            'domainid' : domainId,
            'endport' : endPort,
            'icmpcode' : icmpCode,
            'icmptype' : icmpType,
            'projectid' : projectId,
            'protocol' : protocol,
            'securitygroupid' : securityGroupId,
            'securitygroupname' : securityGroupName,
            'startport' : startPort,
            'usersecuritygrouplist' : userSecurityGroupList,
        })
    
    def revokeSecurityGroupEgress(self, id):
        '''
        Deletes a particular egress rule from this security group
        '''

        return self.request("revokeSecurityGroupEgress", {
            'id' : id,
        })
    
    def listSecurityGroups(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", securityGroupName = "", tags = "", virtualMachineId = ""):
        '''
        Lists security groups
        '''

        return self.request("listSecurityGroups", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'securitygroupname' : securityGroupName,
            'tags' : tags,
            'virtualmachineid' : virtualMachineId,
        })
    
    def listUsers(self, account = "", accountType = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", state = "", userName = ""):
        '''
        Lists user accounts
        '''

        return self.request("listUsers", {
            'account' : account,
            'accounttype' : accountType,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'state' : state,
            'username' : userName,
        })
    
    def disableUser(self, id):
        '''
        Disables a user account
        '''

        return self.request("disableUser", {
            'id' : id,
        })
    
    def enableUser(self, id):
        '''
        Enables a user account
        '''

        return self.request("enableUser", {
            'id' : id,
        })
    
    def addVpnUser(self, password, userName, account = "", domainId = "", projectId = ""):
        '''
        Adds vpn users
        '''

        return self.request("addVpnUser", {
            'password' : password,
            'username' : userName,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def removeVpnUser(self, userName, account = "", domainId = "", projectId = ""):
        '''
        Removes vpn user
        '''

        return self.request("removeVpnUser", {
            'username' : userName,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def listVpnUsers(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", userName = ""):
        '''
        Lists vpn users
        '''

        return self.request("listVpnUsers", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'username' : userName,
        })
    
    def createSnapshot(self, volumeId, account = "", domainId = "", policyId = ""):
        '''
        Creates an instant snapshot of a volume.
        '''

        return self.request("createSnapshot", {
            'volumeid' : volumeId,
            'account' : account,
            'domainid' : domainId,
            'policyid' : policyId,
        })
    
    def listSnapshots(self, account = "", domainId = "", id = "", intervalType = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = "", snapshotType = "", tags = "", volumeId = ""):
        '''
        Lists all available snapshots for the account.
        '''

        return self.request("listSnapshots", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'intervaltype' : intervalType,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'snapshottype' : snapshotType,
            'tags' : tags,
            'volumeid' : volumeId,
        })
    
    def deleteSnapshot(self, id):
        '''
        Deletes a snapshot of a disk volume.
        '''

        return self.request("deleteSnapshot", {
            'id' : id,
        })
    
    def createSnapshotPolicy(self, intervalType, maxSnaps, schedule, timezone, volumeId):
        '''
        Creates a snapshot policy for the account.
        '''

        return self.request("createSnapshotPolicy", {
            'intervaltype' : intervalType,
            'maxsnaps' : maxSnaps,
            'schedule' : schedule,
            'timezone' : timezone,
            'volumeid' : volumeId,
        })
    
    def deleteSnapshotPolicies(self, id = "", ids = ""):
        '''
        Deletes snapshot policies for the account.
        '''

        return self.request("deleteSnapshotPolicies", {
            'id' : id,
            'ids' : ids,
        })
    
    def listSnapshotPolicies(self, volumeId, keyword = "", page = "", pageSize = ""):
        '''
        Lists snapshot policies.
        '''

        return self.request("listSnapshotPolicies", {
            'volumeid' : volumeId,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listPortForwardingRules(self, account = "", domainId = "", id = "", ipAddressId = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", tags = ""):
        '''
        Lists all port forwarding rules for an IP address.
        '''

        return self.request("listPortForwardingRules", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'ipaddressid' : ipAddressId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'tags' : tags,
        })
    
    def createPortForwardingRule(self, ipAddressId, privatePort, protocol, publicPort, virtualMachineId, cidrList = "", networkId = "", openFirewall = "", privateEndPort = "", publicEndPort = ""):
        '''
        Creates a port forwarding rule
        '''

        return self.request("createPortForwardingRule", {
            'ipaddressid' : ipAddressId,
            'privateport' : privatePort,
            'protocol' : protocol,
            'publicport' : publicPort,
            'virtualmachineid' : virtualMachineId,
            'cidrlist' : cidrList,
            'networkid' : networkId,
            'openfirewall' : openFirewall,
            'privateendport' : privateEndPort,
            'publicendport' : publicEndPort,
        })
    
    def deletePortForwardingRule(self, id):
        '''
        Deletes a port forwarding rule
        '''

        return self.request("deletePortForwardingRule", {
            'id' : id,
        })
    
    def createFirewallRule(self, ipAddressId, protocol, cidrList = "", endPort = "", icmpCode = "", icmpType = "", startPort = "", type = ""):
        '''
        Creates a firewall rule for a given ip address
        '''

        return self.request("createFirewallRule", {
            'ipaddressid' : ipAddressId,
            'protocol' : protocol,
            'cidrlist' : cidrList,
            'endport' : endPort,
            'icmpcode' : icmpCode,
            'icmptype' : icmpType,
            'startport' : startPort,
            'type' : type,
        })
    
    def deleteFirewallRule(self, id):
        '''
        Deletes a firewall rule
        '''

        return self.request("deleteFirewallRule", {
            'id' : id,
        })
    
    def listFirewallRules(self, account = "", domainId = "", id = "", ipAddressId = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", tags = ""):
        '''
        Lists all firewall rules for an IP address.
        '''

        return self.request("listFirewallRules", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'ipaddressid' : ipAddressId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'tags' : tags,
        })
    
    def disableAccount(self, lock, account = "", domainId = "", id = ""):
        '''
        Disables an account
        '''

        return self.request("disableAccount", {
            'lock' : lock,
            'account' : account,
            'domainid' : domainId,
            'id' : id,
        })
    
    def enableAccount(self, account = "", domainId = "", id = ""):
        '''
        Enables an account
        '''

        return self.request("enableAccount", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
        })
    
    def listAccounts(self, accountType = "", domainId = "", id = "", isCleanUpRequired = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", state = ""):
        '''
        Lists accounts and provides detailed account information for listed accounts
        '''

        return self.request("listAccounts", {
            'accounttype' : accountType,
            'domainid' : domainId,
            'id' : id,
            'iscleanuprequired' : isCleanUpRequired,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'state' : state,
        })
    
    def addAccountToProject(self, projectId, account = "", email = ""):
        '''
        Adds acoount to a project
        '''

        return self.request("addAccountToProject", {
            'projectid' : projectId,
            'account' : account,
            'email' : email,
        })
    
    def deleteAccountFromProject(self, account, projectId):
        '''
        Deletes account from the project
        '''

        return self.request("deleteAccountFromProject", {
            'account' : account,
            'projectid' : projectId,
        })
    
    def listProjectAccounts(self, projectId, account = "", keyword = "", page = "", pageSize = "", role = ""):
        '''
        Lists project's accounts
        '''

        return self.request("listProjectAccounts", {
            'projectid' : projectId,
            'account' : account,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'role' : role,
        })
    
    def enableStaticNat(self, ipAddressId, virtualMachineId, networkId = ""):
        '''
        Enables static nat for given ip address
        '''

        return self.request("enableStaticNat", {
            'ipaddressid' : ipAddressId,
            'virtualmachineid' : virtualMachineId,
            'networkid' : networkId,
        })
    
    def createIpForwardingRule(self, ipAddressId, protocol, startPort, cidrList = "", endPort = "", openFirewall = ""):
        '''
        Creates an ip forwarding rule
        '''

        return self.request("createIpForwardingRule", {
            'ipaddressid' : ipAddressId,
            'protocol' : protocol,
            'startport' : startPort,
            'cidrlist' : cidrList,
            'endport' : endPort,
            'openfirewall' : openFirewall,
        })
    
    def deleteIpForwardingRule(self, id):
        '''
        Deletes an ip forwarding rule
        '''

        return self.request("deleteIpForwardingRule", {
            'id' : id,
        })
    
    def listIpForwardingRules(self, account = "", domainId = "", id = "", ipAddressId = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", virtualMachineId = ""):
        '''
        List the ip forwarding rules
        '''

        return self.request("listIpForwardingRules", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'ipaddressid' : ipAddressId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'virtualmachineid' : virtualMachineId,
        })
    
    def disableStaticNat(self, ipAddressId):
        '''
        Disables static rule for given ip address
        '''

        return self.request("disableStaticNat", {
            'ipaddressid' : ipAddressId,
        })
    
    def createInstanceGroup(self, name, account = "", domainId = "", projectId = ""):
        '''
        Creates a vm group
        '''

        return self.request("createInstanceGroup", {
            'name' : name,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def deleteInstanceGroup(self, id):
        '''
        Deletes a vm group
        '''

        return self.request("deleteInstanceGroup", {
            'id' : id,
        })
    
    def updateInstanceGroup(self, id, name = ""):
        '''
        Updates a vm group
        '''

        return self.request("updateInstanceGroup", {
            'id' : id,
            'name' : name,
        })
    
    def listInstanceGroups(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = ""):
        '''
        Lists vm groups
        '''

        return self.request("listInstanceGroups", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
        })
    
    def createSSHKeyPair(self, name, account = "", domainId = "", projectId = ""):
        '''
        Create a new keypair and returns the private key
        '''

        return self.request("createSSHKeyPair", {
            'name' : name,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def deleteSSHKeyPair(self, name, account = "", domainId = "", projectId = ""):
        '''
        Deletes a keypair by name
        '''

        return self.request("deleteSSHKeyPair", {
            'name' : name,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def listSSHKeyPairs(self, account = "", domainId = "", fingerprint = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = ""):
        '''
        List registered keypairs
        '''

        return self.request("listSSHKeyPairs", {
            'account' : account,
            'domainid' : domainId,
            'fingerprint' : fingerprint,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
        })
    
    def createTags(self, resourceIds, resourceType, tags, customer = ""):
        '''
        Creates resource tag(s)
        '''

        return self.request("createTags", {
            'resourceids' : resourceIds,
            'resourcetype' : resourceType,
            'tags' : tags,
            'customer' : customer,
        })
    
    def deleteTags(self, resourceIds, resourceType, tags = ""):
        '''
        Deleting resource tag(s)
        '''

        return self.request("deleteTags", {
            'resourceids' : resourceIds,
            'resourcetype' : resourceType,
            'tags' : tags,
        })
    
    def listTags(self, account = "", customer = "", domainId = "", isRecursive = "", key = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", resourceid = "", resourceType = "", value = ""):
        '''
        List resource tag(s)
        '''

        return self.request("listTags", {
            'account' : account,
            'customer' : customer,
            'domainid' : domainId,
            'isrecursive' : isRecursive,
            'key' : key,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'resourceid' : resourceid,
            'resourcetype' : resourceType,
            'value' : value,
        })
    
    def registerTemplate(self, displayText, format, hypervisor, name, osTypeId, url, zoneId, account = "", bits = "", checksum = "", details = "", domainId = "", isExtractable = "", isFeatured = "", isPublic = "", passwordEnabled = "", projectId = "", requireShvm = "", sshkeyEnabled = "", templateTag = ""):
        '''
        Registers an existing template into the CloudStack cloud.
        '''

        return self.request("registerTemplate", {
            'displaytext' : displayText,
            'format' : format,
            'hypervisor' : hypervisor,
            'name' : name,
            'ostypeid' : osTypeId,
            'url' : url,
            'zoneid' : zoneId,
            'account' : account,
            'bits' : bits,
            'checksum' : checksum,
            'details' : details,
            'domainid' : domainId,
            'isextractable' : isExtractable,
            'isfeatured' : isFeatured,
            'ispublic' : isPublic,
            'passwordenabled' : passwordEnabled,
            'projectid' : projectId,
            'requireshvm' : requireShvm,
            'sshkeyenabled' : sshkeyEnabled,
            'templatetag' : templateTag,
        })
    
    def registerIso(self, displayText, name, url, zoneId, account = "", bootable = "", checksum = "", domainId = "", isExtractable = "", isFeatured = "", isPublic = "", osTypeId = "", projectId = ""):
        '''
        Registers an existing ISO into the CloudStack Cloud.
        '''

        return self.request("registerIso", {
            'displaytext' : displayText,
            'name' : name,
            'url' : url,
            'zoneid' : zoneId,
            'account' : account,
            'bootable' : bootable,
            'checksum' : checksum,
            'domainid' : domainId,
            'isextractable' : isExtractable,
            'isfeatured' : isFeatured,
            'ispublic' : isPublic,
            'ostypeid' : osTypeId,
            'projectid' : projectId,
        })
    
    def registerSSHKeyPair(self, name, publicKey, account = "", domainId = "", projectId = ""):
        '''
        Register a public key in a keypair under a certain name
        '''

        return self.request("registerSSHKeyPair", {
            'name' : name,
            'publickey' : publicKey,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def updateResourceLimit(self, resourceType, account = "", domainId = "", max = "", projectId = ""):
        '''
        Updates resource limits for an account or domain.
        '''

        return self.request("updateResourceLimit", {
            'resourcetype' : resourceType,
            'account' : account,
            'domainid' : domainId,
            'max' : max,
            'projectid' : projectId,
        })
    
    def updateResourceCount(self, domainId, account = "", projectId = "", resourceType = ""):
        '''
        Recalculate and update resource count for an account or domain.
        '''

        return self.request("updateResourceCount", {
            'domainid' : domainId,
            'account' : account,
            'projectid' : projectId,
            'resourcetype' : resourceType,
        })
    
    def listResourceLimits(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", resourceType = ""):
        '''
        Lists resource limits.
        '''

        return self.request("listResourceLimits", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'resourcetype' : resourceType,
        })
    
    def associateIpAddress(self, account = "", domainId = "", networkId = "", projectId = "", vpcId = "", zoneId = ""):
        '''
        Acquires and associates a public IP to an account.
        '''

        return self.request("associateIpAddress", {
            'account' : account,
            'domainid' : domainId,
            'networkid' : networkId,
            'projectid' : projectId,
            'vpcid' : vpcId,
            'zoneid' : zoneId,
        })
    
    def disassociateIpAddress(self, id):
        '''
        Disassociates an ip address from the account.
        '''

        return self.request("disassociateIpAddress", {
            'id' : id,
        })
    
    def listPublicIpAddresses(self, account = "", allocatedOnly = "", associatedNetworkId = "", domainId = "", forLoadBalancing = "", forVirtualNetwork = "", id = "", ipAddress = "", isRecursive = "", isSourceNat = "", isStaticNat = "", keyword = "", listAll = "", page = "", pageSize = "", physicalNetworkId = "", projectId = "", tags = "", vlanId = "", vpcId = "", zoneId = ""):
        '''
        Lists all public ip addresses
        '''

        return self.request("listPublicIpAddresses", {
            'account' : account,
            'allocatedonly' : allocatedOnly,
            'associatednetworkid' : associatedNetworkId,
            'domainid' : domainId,
            'forloadbalancing' : forLoadBalancing,
            'forvirtualnetwork' : forVirtualNetwork,
            'id' : id,
            'ipaddress' : ipAddress,
            'isrecursive' : isRecursive,
            'issourcenat' : isSourceNat,
            'isstaticnat' : isStaticNat,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'physicalnetworkid' : physicalNetworkId,
            'projectid' : projectId,
            'tags' : tags,
            'vlanid' : vlanId,
            'vpcid' : vpcId,
            'zoneid' : zoneId,
        })
    
    def listOsTypes(self, description = "", id = "", keyword = "", osCategoryId = "", page = "", pageSize = ""):
        '''
        Lists all supported OS types for this cloud.
        '''

        return self.request("listOsTypes", {
            'description' : description,
            'id' : id,
            'keyword' : keyword,
            'oscategoryid' : osCategoryId,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listOsCategories(self, id = "", keyword = "", name = "", page = "", pageSize = ""):
        '''
        Lists all supported OS categories for this cloud.
        '''

        return self.request("listOsCategories", {
            'id' : id,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listEvents(self, account = "", domainId = "", duration = "", endDate = "", entryTime = "", id = "", isRecursive = "", keyword = "", level = "", listAll = "", page = "", pageSize = "", projectId = "", startDate = "", type = ""):
        '''
        A command to list events.
        '''

        return self.request("listEvents", {
            'account' : account,
            'domainid' : domainId,
            'duration' : duration,
            'enddate' : endDate,
            'entrytime' : entryTime,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'level' : level,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'startdate' : startDate,
            'type' : type,
        })
    
    def listEventTypes(self, ):
        '''
        List Event Types
        '''

        return self.request("listEventTypes", {
        })
    
    def listDomains(self, id = "", keyword = "", level = "", listAll = "", name = "", page = "", pageSize = ""):
        '''
        Lists domains and provides detailed information for listed domains
        '''

        return self.request("listDomains", {
            'id' : id,
            'keyword' : keyword,
            'level' : level,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listDomainChildren(self, id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = ""):
        '''
        Lists all children domains belonging to a specified domain
        '''

        return self.request("listDomainChildren", {
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def queryAsyncJobResult(self, jobId):
        '''
        Retrieves the current status of asynchronous job.
        '''

        return self.request("queryAsyncJobResult", {
            'jobid' : jobId,
        })
    
    def listAsyncJobs(self, account = "", domainId = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", startDate = ""):
        '''
        Lists all pending asynchronous jobs for the account.
        '''

        return self.request("listAsyncJobs", {
            'account' : account,
            'domainid' : domainId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'startdate' : startDate,
        })
    
    def listZones(self, available = "", domainId = "", id = "", keyword = "", page = "", pageSize = "", showCapacities = ""):
        '''
        Lists zones
        '''

        return self.request("listZones", {
            'available' : available,
            'domainid' : domainId,
            'id' : id,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'showcapacities' : showCapacities,
        })
    
    def listServiceOfferings(self, domainId = "", id = "", isSystem = "", keyword = "", name = "", page = "", pageSize = "", systemVmType = "", virtualMachineId = ""):
        '''
        Lists all available service offerings.
        '''

        return self.request("listServiceOfferings", {
            'domainid' : domainId,
            'id' : id,
            'issystem' : isSystem,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'systemvmtype' : systemVmType,
            'virtualmachineid' : virtualMachineId,
        })
    
    def logout(self, ):
        '''
        Logs out the user
        '''

        return self.request("logout", {
        })
    
    def login(self, userName, password, domain = "", domainId = ""):
        '''
        Logs a user into the CloudStack. A successful login attempt will generate a JSESSIONID cookie value that can be passed in subsequent Query command calls until the "logout" command has been issued or the session has expired.
        '''

        return self.request("login", {
            'username' : userName,
            'password' : password,
            'domain' : domain,
            'domainId' : domainId,
        })
    
    def listHypervisors(self, zoneId = ""):
        '''
        List hypervisors
        '''

        return self.request("listHypervisors", {
            'zoneid' : zoneId,
        })
    
    def listDiskOfferings(self, domainId = "", id = "", keyword = "", name = "", page = "", pageSize = ""):
        '''
        Lists all available disk offerings.
        '''

        return self.request("listDiskOfferings", {
            'domainid' : domainId,
            'id' : id,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listCapabilities(self, ):
        '''
        Lists capabilities
        '''

        return self.request("listCapabilities", {
        })
    
    def getCloudIdentifier(self, userId):
        '''
        Retrieves a cloud identifier.
        '''

        return self.request("getCloudIdentifier", {
            'userid' : userId,
        })
    
