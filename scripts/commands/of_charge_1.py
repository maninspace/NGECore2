import sys

def setup(core, actor, buff):
	return
	
def run(core, actor, target, commandString):
	core.buffService.addBuffToCreature(actor, 'of_charge_1')
	group = core.objectService.getObject(actor.getGroupId())
	for creature in group.getMemberList():
		core.buffService.addBuffToCreature(creature, 'of_charge_1')
	return
	