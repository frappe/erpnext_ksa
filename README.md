## ERPNext KSA

App to hold regional code for Kingdom of Saudi Arabia, built on top of ERPNext.

### Introduction

ERPNext KSA holds regional customizations for Kingdom of Saudi Arabia such as several custom fields for doctypes, some custom print formats, doctypes for VAT Settings and more. It is built on Frappe, a full-stack, meta-data driven, web framework, and integrates seamlessly with ERPNext, the most agile ERP software.


### Installation

Using bench, [install ERPNext](https://github.com/frappe/bench#installation) as mentioned here.

Once ERPNext is installed, add ERPNext KSA app to your bench by running

```sh
$ bench get-app https://github.com/DeeMysterio/erpnext_ksa.git
```

After that, you can install the app on required site (let's say demo.com )by running

```sh
$ bench --site demo.com install-app erpnext_ksa
```

### License

GNU GPL V3. See [license.txt](https://github.com/DeeMysterio/erpnext_ksa/blob/develop/license.txt) for more information.
