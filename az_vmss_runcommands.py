# import os
import argparse
from dotenv import load_dotenv
from azure.mgmt.compute import ComputeManagementClient
# from azure.mgmt.compute.models import RunCommandInput
from azure.identity import DefaultAzureCredential
from resource_graph_query import run_azure_rg_query

def run_commands_on_vmss(resource_group:str, subscription_id:str, vmss_name:str):
	"""
	Execute run commands on Azure using Compute Management Client class
	:return:
	"""
	credential = DefaultAzureCredential()
	compute_mgmt_client = ComputeManagementClient(credential=credential, subscription_id=subscription_id)

	# Get all VM instances in the VMSS
	vmss_instances = compute_mgmt_client.virtual_machine_scale_set_vms.list(resource_group_name=resource_group,
															virtual_machine_scale_set_name = vmss_name)
	instance_details = []
	for instance in vmss_instances:
		# print(instance)
		instances = {
			'name': instance.name,
			'id': instance.id,
			'instance_id': instance.instance_id
		}
		instance_details.append(instances)

	# print(f'instance details : {instance_details}')


	for vmss_in in instance_details:
		# Define the command parameters
		run_command_parameters = {
			'command_id':'RunShellScript',
			'script': ['df -hT']
		}
		response = compute_mgmt_client.virtual_machine_scale_set_vms.begin_run_command(
			resource_group_name=resource_group, vm_scale_set_name=vmss_name,
			instance_id= vmss_in['instance_id'], parameters=run_command_parameters
		)


		# Optionally, print the command output
		result = response.result()
		if result.value[0].code == "ProvisioningState/succeeded":
			# print(result.value[0].message)
			print(f"Run command execution in instance {vmss_in['name']} of {vmss_name} VMSS completed successfully")
		else:
			print('Something went wrong!!')



def main():
	"""
	Execute program
	:return:
	"""
	load_dotenv()
	parser = argparse.ArgumentParser("Execute Run commands on an Azure VM")
	parser.add_argument("--subscription_name", help="Azuer Subscription name", required=True, type=str)
	parser.add_argument("--vmss_name", help="Azure VM name",required=True, type=str)
	parser.add_argument("--resource_group", help="Azure resource group name", type=str, required=True)

	args = parser.parse_args()

	subscription_name =args.subscription_name
	vmss_name = args.vmss_name
	resource_group = args.resource_group

	subscription_id = run_azure_rg_query(subscription_name=subscription_name)

	run_commands_on_vmss(subscription_id=subscription_id, resource_group=resource_group, vmss_name=vmss_name)


if __name__ == "__main__":
	main()

