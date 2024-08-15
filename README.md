# azure-runcommands-on-vm-vmss-with-python-sdk
Code to execute run commands on Azure VMs and VMSS using python sdks

# Why?

* In Enterprises / Companies There will be multiple VMs or VMSS or both running 
* These might be maintained and updated regularly or not
* Sometimes there will be a requirement to stop some services or so
* This can be used for the purpose


# Inputs

| Inputs | Description | Required |
|--------|-------------|----------|
| subscription_name | Azure subscription name | :heavy_check_mark: |
| resource_group | Azure resource group name | :heavy_check_mark: |
| vm_name or vmss_name | Azure Vm or VMSS name | :heavy_check_mark: |


# How 

* This program uses Azure Python SDKs to execute run commands


# How to run locally

* Clone this repo and change directory to `azure-runcommands-on-vm-vmss-with-python-sdk`

* Get the required parameters and run the code using below commands

* python az_vm_runcommands.py --subscription_name `<Subscription Name>` --resource_group `<resource group name>` --vm_name `<VM name>`

* python az_vmss_runcommands.py --subscription_name `<Subscription Name>` --resource_group `<resource group name>` --vmss_name `<VMSS name>`


# References

* [azure-mgmt-resourcegraph](https://learn.microsoft.com/en-us/python/api/overview/azure/mgmt-resourcegraph-readme?view=azure-python)
  This SDK is used to determine the subscription id from subscription name

* [azure-identity](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity?view=azure-python)
  This is used for Authentication purposes

* [azure-mgmt-compute](https://learn.microsoft.com/en-us/python/api/overview/azure/mgmt-compute-readme?view=azure-python)
  This package is used to execute the run commands on resources
* [python/azure-mgmt-compute](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-mgmt-compute/32.0.0/azure.mgmt.compute.html#azure.mgmt.compute.ComputeManagementClient.virtual_machine_run_commands)
