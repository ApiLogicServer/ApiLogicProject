# Welcome to API Logic Server

Use API Logic Server to create customizable database web app projects _instantly_ from your database schema, providing:

* __API__ - an endpoint for each table, with filtering, sorting, pagination and related data access

* __Admin UI__ - multi-page / multi-table apps, with page navigations and automatic joins

* __Logic Automation__ - using unique rules, extensible with Python

Created projects are customizable with your IDE, such as VSCode.

This project is the sample project, provided so you can explore API Logic Server.

&nbsp;

# API Logic Server Background

### Motivation - not instant, propietary IDE, no logic automation

We looked at approaches for building database systems:

<br/>

__Frameworks__

Frameworks like Flask or Django enable you to build a single endpoint or _Hello World_ page, but a __multi-endpoint__ API and __multi-page__ application would take __weeks__ or more.

<br/>

__Low Code Tools__

These are great for building great UIs, but

* Want a multi-page app -- __no screen painting__
* Want to __preserve dev tools__ - VSCode, PyCharm, git, etc
* Need an answer for __backend logic__ (it's nearly half the effort)

&nbsp;

### Our Approach: Instant, Customizable, Logic Automation

API Logic Server is an open source Python project, consisting of:

* a set of runtimes (SAFRS API, Flask, SQLAlchemy ORM, rule engine) for project execution, plus 

* a CLI (Command Language Interface) to create executable projects, which can be customized in an IDE such as VSCode or PyCharm

It runs as a standard pip install, or under Docker. After installation, you use the CLI create a project like this:

Use API Logic Server to instantly create customizable database web app projects, providing API, Admin UI, and unique declarative business logic.  Created projects are customizable with your IDE, such as VSCode.

```
ApiLogicServer create --project_name=ApiLogicServer-Explore db_url=
```

> API Logic Server reads your schema, and creates the executable project you see here.

&nbsp;

### What's Already Happened

We've already executed the `ApiLogicServer create` command, and uploaded the project to GitHub, [like this](https://valhuber.github.io/ApiLogicServer/Manage-GitHub/#create-an-api-logic-server-project).  You could clone this and open it locally.  But an even faster way - _with no install_ - is to follow the Exploration Guide, below.

&nbsp;

# Exploring API Logic Server

The procedure below is the fastest way to explore API Logic Server:

1. Open this project in Codespaces - no install required!
2. [Run the Tutorial](Tutorial.md)]

&nbsp;

### 1. Open in Codespaces

Here are some instructions you can use to explore API Logic Server running under CodeSpaces.


__1. Load your API Logic Server Project__

Access this GitHub project with Codespaces, as follows:

<figure><img src="https://github.com/valhuber/apilogicserver/wiki/images/git-codespaces/open-org-on-codespaces.png?raw=true"></figure> 

> You will now see the sample project - running in VSCode, _in the Browser._  That's just what you see... 

> Behind the scenes, Codespaces has requisitioned a cloud machine, and loaded your project - with a _complete development environment_ - Python, your dependencies, git, etc.  

> You are attached to this machine in your Browser, running VSCode.

> Pretty remarkable.

&nbsp;

__2. Configure a Port__

<figure><img src="https://github.com/valhuber/apilogicserver/wiki/images/git-codespaces/create-port-launch.png?raw=true"></figure>

__3. Configure the pre-created `Codespaces-ApiLogicServer` launch configuration__ (see above)

* Make the port __public__
* Note that the trailing slash, and the `https://` are removed

__4. Start the Server__ using the provided Launch Configuration = `Codespaces-ApiLogicServer`

__5. Open the Browser__

Click the globe, as shown above.  This should start your Browser, and the links on the left (Customer etc) should return data.


&nbsp;

### 2. Run the Tutorial

Now, [open the Tutorial](Tutorial.md).  You can do this on the current page, or within the opened project.

You'll be able to explore 2 key aspects:

* __Initial Automation__ - API and UI creation are automated from the data model. So, later, you'd see this level of automation for your own databases.

* __Customization and Debugging__ - this sample also includes customizations for extending the API and declaring logic, and how to use VSCode to debug these.  The Tutorial will clearly identify such pre-built customizations.


&nbsp;
---

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
