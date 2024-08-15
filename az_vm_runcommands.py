import os
import argparse
from dotenv import load_dotenv
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import RunCommandInput
from azure.identity import DefaultAzureCredential
from resource_graph_query import run_azure_rg_query

def run_commands_on_vm(resource_group:str, subscription_id:str, vm_name:str):
	"""
	Execute run commands on Azure using Compute Management Client class
	:return:
	"""
	credential = DefaultAzureCredential()
	compute_mgmt_client = ComputeManagementClient(credential=credential, subscription_id=subscription_id)

	# Define the command parameters
	run_command_parameters = RunCommandInput(
		command_id='RunShellScript',
		script=['sudo systemctl start jenkins']
	)
	print(f'Executing Run commands on {vm_name} VM of resource group {resource_group}')
	response = compute_mgmt_client.virtual_machines.begin_run_command(resource_group_name=resource_group,
													   vm_name=vm_name,parameters=run_command_parameters)

	result = response.result()
	if result.value[0].code == "ProvisioningState/succeeded":
		print(f"Run command execution in VM {vm_name} of resource group {resource_group} completed successfully")
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
	parser.add_argument("--vm_name", help="Azure VM name",required=True, type=str)
	parser.add_argument("--resource_group", help="Azure resource group name", type=str, required=True)

	args = parser.parse_args()

	subscription_name =args.subscription_name
	vm_name = args.vm_name
	resource_group = args.resource_group

	subscription_id = run_azure_rg_query(subscription_name=subscription_name)

	run_commands_on_vm(subscription_id=subscription_id, resource_group=resource_group, vm_name=vm_name)


if __name__ == "__main__":
	main()

