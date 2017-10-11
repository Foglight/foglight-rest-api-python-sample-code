from __init__ import executeget
from __init__ import executepost
from __init__ import executelogin
from __init__ import config

#
# Before testing: you need to set both config['Global']['api.username'] and config['Global']['api.password']) in __init__.cfg
# For some of the testing refers to config[XXX][XXX], you also need to set the value in __init.cfg before testing.
#
json_response = executelogin(username=config['Global']['api.username'],
                   password=config['Global']['api.password'])
config['Global']['api.token'] = json_response['data']['token']

# Agent
print(executeget("/agent/allAgents"))
print(executeget("/agent/active"))
print(executeget("/agent/inactive"))
# print(executeget("/agent/agentId/" + config['Agent']['api.agent.agentId']))

# Alarm
print(executeget("/alarm/current"))
print(executeget("/alarm/history"))
# print(executeget("/alarm/" + config['Alarm']['api.alarm.alarmId']))
# print(executeget("/alarm/ruleId/" + config['Alarm']['api.alarm.ruleId']))
# print(executeget("/alarm/ack/" + config['Alarm']['api.alarm.ack.alarmId']))
# print(executeget("/alarm/clear/" + config['Alarm']['api.alarm.clear.alarmId']))
# print(executeget("/alarm/current/" + config['Alarm']['api.alarm.topologyId']))
# print(executeget("/alarm/history/" + config['Alarm']['api.alarm.topologyId']))

# Cartridge
print(executeget("/cartridge/allCartridges"))
print(executeget("/cartridge/allCartridges/core"))
print(executeget("/cartridge/allCartridges/nonCore"))

# Registry
print(executeget("/registry/allRegistries"))

# Remote Client
print(executeget("/remoteClient/allRemoteClients"))

# Rule
print(executeget("/rule/allRules"))
# print(executeget("/rule/" + config['Rule']['api.rule.ruleId']))

# Subscribe Alarm

print(executeget("/subscription/list"))
print(executeget("/subscription/alarm/subscribe"))
print(executeget("/subscription/disconnect/all"))
# print(executeget("/subscription/alarm/subscribe/" + config['SubscribeAlarm']['api.subscribe.topologyId']))

# Topology
# print(executeget("/topology/" + config['Topology']['api.topology.topologyId']))
# print(executeget("/topology/" + config['Topology']['api.topology.topologyId'] + "/cpus/utilization"))
# print(executeget("/topology/" + config['Topology']['api.topology.topologyId'] + "/paths?path=name&path=uniqueId&path=utilization"))
# print(executeget("/topology/topologyId/" + config['Topology']['api.topology.topologyObjectId']))
# print(executeget("/topology/topologyIds?Id=" + config['Topology']['api.topology.topologyObjectId']))
print(executepost("/topology/batchQuery",
                 data={"includes":[{"ids":[config['Topology']['api.topology.topologyObjectId']],"observationName":"utilization"}],
                        "endTime":1477987660722}))
print(executepost("/topology/query", data={"queryText":"!Host"}))

# Topology Type
# print(executeget("/type/" + config['TopologyType']['api.topologytype.typeName']))
# print(executeget("/type/" + config['TopologyType']['api.topologytype.typeName'] + "/super"))
# print(executeget("/type/" + config['TopologyType']['api.topologytype.typeName'] + "/instances"))

# User Information
print(executeget("/user/current"))

# Push Alarm: get first topology object id and rule id since there is no validation for the reference of these two
push_alarm_json = executeget("/type/" + config['TopologyType']['api.topologytype.typeName'] + "/instances")
topology_object_id = push_alarm_json['data'][0]['uniqueId']
push_alarm_json = executeget("/rule/allRules")
rule_id = push_alarm_json['data'][0]['id']
if rule_id:
    print(executepost("/alarm/pushAlarm",
            data={"alarmMessage":"This is a test alarm message from postman",
                  "severity":"2",
                  "topologyObjectId":topology_object_id}))
else:
    print(executepost("/alarm/pushAlarm",
            data={"alarmMessage":"This is a test alarm message from postman",
                  "severity":"2",
                  "topologyObjectId":topology_object_id,
                  "ruleId":rule_id}))

# Push Data: import the topology type into Foglight before you start this query
# <!DOCTYPE types SYSTEM "../dtd/topology-types.dtd">
# <types>
#    <type name='PushDataTest1' extends='TopologyObject'>
#		<property name='name' type='String' is-identity='true'/>
#		<property name='testMetric' type='Metric' is-containment='true' unit-name='count' />
#		<property name='testObservations' type='TestObservation1' is-containment='true' unit-name='count' />
#	</type>
#	<type name='TestObservation1' extends='ComplexObservation'>
#		<property name='current' type='TestObservationValue1' is-many='false' is-containment='true' />
#		<property name='latest' type='TestObservationValue1' is-many='false' is-containment='true' />
#		<property name='history' type='TestObservationValue1' is-many='true' is-containment='true' />
#	</type>
#	<type name='TestObservationValue1' extends='ObservedValue'>
#		<property name='value' type='TestObject1' is-containment='true'/>
#	</type>
#	<type name="TestObject1" extends="DataObject">
#		<property name='testName' type='String' />
#		<property name='createDate' type='Date' />
#		<property name='createTime' type='Double' />
#	</type>
#</types>
print(executepost("/topology/pushData",
                  data={"data":[{
                            "typeName": "PushDataTest1",
                            "properties": {
                              "name" : "TestData1",
                              "testMetric": 90.0,
                              "testObservations": {
                                "testName" : "testObservation1",
                                "createDate": 1500775583000,
                                "createTime": 1500775583000
                              }
                            }
                          }],
                          "startTime": 1500775583000,
                          "endTime": 1500861983000
                        }))