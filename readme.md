# Welcome to API Logic Server

To explore API Logic Server:

* Open this project in Codespaces - no install required!

&nbsp;

### Using Codespaces

This GitHub project enables you to use VSCode in your Browser to develop on rapidly deployed docker containers.  It's quite remarkable.  It is entirely interoperable with VSCode operations on your local machine.

Here are some instructions you can use to explore API Logic Server running under CodeSpaces.


__1. Load your ApiLogicProject-GitHub__

Access this GitHub project with Codespaces, as follows:

<figure><img src="https://github.com/valhuber/apilogicserver/wiki/images/git-codespaces/open-on-codespaces.png?raw=true"></figure> 


__2. Configure a Port__

<figure><img src="https://github.com/valhuber/apilogicserver/wiki/images/git-codespaces/create-port-launch.png?raw=true"></figure>

__3. Configure the pre-created `Codespaces-ApiLogicServer` launch configuration__ (see above)

* Make the port __public__
* Note that the trailing slash, and the `https://` are removed

__4. Start the Server__ using the provided Launch Configuration = `Codespaces-ApiLogicServer`

__5. Open the Browser__

Click the globe, as shown above.  This should start your Browser, and the links on the left (Customer etc) should return data.


&nbsp;

### Run the Tutorial

Now, [open the Tutorial](Tutorial.md).

&nbsp;
---

&nbsp;

&nbsp;
# Readme - API Logic Project

This API Logic Project was created by the API Logic Server with the `ApiLogicServer create` command.  

Edit / extend this readme as desired.

&nbsp;&nbsp;

# Appendices

Here is some background about API Logic Server.


&nbsp;&nbsp;

## Project Information

| About                    | Info                               |
|:-------------------------|:-----------------------------------|
| Created                  | August 18, 2022 07:24:31                      |
| API Logic Server Version | 5.03.34           |
| Created in directory     | ../../servers/ApiLogicProject |
| API Name                 | api          |

&nbsp;&nbsp;


## Key Technologies

API Logic Server is based on the projects shown below.
Consult their documentation for important information.

### SARFS JSON:API Server

[SAFRS: Python OpenAPI & JSON:API Framework](https://github.com/thomaxxl/safrs)

SAFRS is an acronym for SqlAlchemy Flask-Restful Swagger.
The purpose of this framework is to help python developers create
a self-documenting JSON API for sqlalchemy database objects and relationships.

These objects are serialized to JSON and 
created, retrieved, updated and deleted through the JSON API.
Optionally, custom resource object methods can be exposed and invoked using JSON.

Class and method descriptions and examples can be provided
in yaml syntax in the code comments.

The description is parsed and shown in the swagger web interface.
The result is an easy-to-use
swagger/OpenAPI and JSON:API compliant API implementation.

### LogicBank

[Transaction Logic for SQLAlchemy Object Models](https://valhuber.github.io/ApiLogicServer/Logic-Why/)

Use Logic Bank to govern SQLAlchemy update transaction logic - 
multi-table derivations, constraints, and actions such as sending mail or messages. Logic consists of _both:_

*   **Rules - 40X** more concise using a spreadsheet-like paradigm, and

*   **Python - control and extensibility,** using standard tools and techniques

Logic Bank is based on SQLAlchemy - it handles `before_flush` events to enforce your logic.
Your logic therefore applies to any SQLAlchemy-based access - JSON:Api, Admin App, etc.


### SQLAlchemy

[Object Relational Mapping for Python](https://docs.sqlalchemy.org/en/13/).

SQLAlchemy provides Python-friendly database access for Python.

It is used by JSON:Api, Logic Bank, and the Admin App.

SQLAlchemy processing is based on Python `model` classes,
created automatically by API Logic Server from your database,
and saved in the `database` directory.



### Admin App

This generated project also contains a React Admin app:
* Multi-page - including page transitions to "drill down"
* Multi-table - master / details (with tab sheets)
* Intelligent layout - favorite fields first, predictive joins, etc
* Logic Aware - updates are monitored by business logic

&nbsp;&nbsp;

## Project Structure
This project was created with the following directory structure:

| Directory | Usage                         | Key Customization File             | Typical Customization                                                                 |
|:-------------- |:------------------------------|:-----------------------------------|:--------------------------------------------------------------------------------------|
| ```api``` | JSON:API                      | ```api/customize_api.py```         | Add new end points / services                                                         |
| ```database``` | SQLAlchemy Data Model Classes | ```database/customize_models.py``` | Add derived attributes, and relationships missing in the schema                       |
| ```logic``` | Transactional Logic           | ```logic/declare_logic.py```       | Declare multi-table derivations, constraints, and events such as send mail / messages |
| ```ui``` | Admin App                     | ```ui/admin/admin.yaml```          | Control field display - order, captions etc.                                          |
| ```tests``` | Behave Test Suite              | ```tests/api_logic_server_behave/features```          | Declare and implement [Behave Tests](https://valhuber.github.io/ApiLogicServer/Behave/)                                          |
&nbsp;

### Key Customization File - Typical Customization

In the table above, the _Key Customization Files_ are created as stubs, intended for you to add customizations that extend
the created API, Logic and Web App.  Since they are separate files, the project can be
[rebuilt](https://valhuber.github.io/ApiLogicServer/Project-Rebuild/) (e.g., synchronized with a revised schema), preserving your customizations.

Please see the ```nw``` sample for examples of typical customizations.
