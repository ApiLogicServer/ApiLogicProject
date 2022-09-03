# Welcome to API Logic Server

API Logic Server creates __customizable database web app projects:__

* __Creation is Instant:__ create projects with a single command

* __Projects are Highly Functional:__

    * __API__ - an endpoint for each table, with filtering, sorting, pagination and related data access

    * __Admin UI__ - multi-page / multi-table apps, with page navigations and automatic joins


* __Projects are Customizable, using _your IDE_:__ such as VSCode, PyCharm, etc, for familiar edit/debug services

* __Business Logic Automation:__ using unique rules, extensible with Python

Extensive [documentation is available here](https://valhuber.github.io/ApiLogicServer/) - checkout the [FAQs](https://valhuber.github.io/ApiLogicServer/FAQ-Frameworks/).

This is the sample project, provided so you can explore API Logic Server in Codespaces -- __zero install.__

&nbsp;

# API Logic Server Background

### Motivation

We looked at approaches for building database systems:  

<br/>

__Frameworks__

Frameworks like Flask or Django enable you to build a single endpoint or _Hello World_ page, but a __multi-endpoint__ API and __multi-page__ application would take __weeks__ or more.

<br/>

__Low Code Tools__

These are great for building great UIs, but

* Want a multi-page app -- __without requiring detail layout for each screen__
* Want to __preserve standard dev tools__ - VSCode, PyCharm, git, etc
* Need an answer for __backend logic__ (it's nearly half the effort)

&nbsp;

### Our Approach: Instant, Standards-based Customization, Logic Automation

API Logic Server is an open source Python project, consisting of:

* a set of runtimes (api, user interface, data access) for project execution, plus 

* a CLI (Command Language Interface) to create executable projects; open them in your IDE (e.g., VSCode, PyCharm) to customize, run and debug 

It runs as a standard Python (`pip`) install, or under Docker. After installation, you use the CLI create a project like this:

```
ApiLogicServer create --project_name=ApiLogicProject db_url=
```
where:

* `ApiLogicServerProject` is the name of your project (a new directory)
* `db_url` is a SQLAlchemy URL identifying your database; the default is pre-supplied sample<br><br>

> :bulb: API Logic Server reads your schema, and creates  executable, customizable projects.  Let's explore the sample now.

&nbsp;

# Exploration Guide

The fastest way - _with __no install___ - is to follow this guide to:

* Open this empty project in Codespaces
* Use `ApiLogicServer create` to create the sample application
* Use the Tutorial to review:
    * The created UI and API
    * Customizing the UI and API with the VSCode editor and debugger
    * Adding Business Logic with the VSCode editor, and debugging it

&nbsp;

### 1. Open in Codespaces

Explore API Logic Server running under CodeSpaces as follows.

&nbsp;

__1. Use your GitHub account__ - no additional sign-up required

__2. Load this project from GitHub__

To access this GitHub project with Codespaces:

1. [Open this page in a ___new window___](https://github.com/ApiLogicServer/ApiLogicProject), and 
2. Click __Open > Codespaces__ as shown below
3. You will see an empty project.  To create the sample, paste the following into the terminal window:

```
ApiLogicServer create --project_name=./ --db_url=
```

where:

   * `project_name` is specified to be the current directory (normally a new directory)

   * `db_url` is specified as the sample (normally a SQLAlchemy URI to your own database)

<figure><img src="https://github.com/valhuber/apilogicserver/wiki/images/git-codespaces/open-on-codespaces.jpg?raw=true"></figure> 

> You will now see the sample project - running in VSCode, _in the Browser._  But that's just what you _see..._

> Behind the scenes, Codespaces has requisitioned a cloud machine, and loaded your project - with a _complete development environment_ - Python, your dependencies, git, etc.  

> You are attached to this machine in your Browser, running VSCode.

> :trophy: Pretty remarkable.

&nbsp;

__3. Add and Configure a Port__

Referring to the figure below, click the __Ports__ tab, and:

1. Add the Port (5656)
2. Make the port __public__ (use right-click to alter the Visibility)

__4. Start the Server__

* Use the pre-defined Launch Configuration

__5. Start the Browser__

* Click the globe (on the Ports tab), as shown below.  This should start your Browser, and the links on the left (Customer etc) should return data.

<figure><img src="https://github.com/valhuber/apilogicserver/wiki/images/git-codespaces/create-port-launch-simple.jpg?raw=true"></figure>


<details markdown>
<summary>If errors, use this procedure</summary>

The above procedure is simplified, based on some assumptions about Codespaces.  If the Browser fails to launch, try the following for explicit specification of the forwarded port:

<figure><img src="https://github.com/valhuber/apilogicserver/wiki/images/git-codespaces/create-port-launch.png?raw=true"></figure>

__4. Configure the pre-created `Codespaces-ApiLogicServer` launch configuration__ (see above)

__5. Start the Server__ using the provided Launch Configuration = `Codespaces-ApiLogicServer`

__6. Open the Browser__

Click the globe, as shown above.  This should start your Browser, and the links on the left (Customer etc) should return data.

</details>

&nbsp;

### 2. Run the Tutorial

The Tutorial will enable you to explore 2 key aspects:

* __Initial Automation__ - API and UI creation are automated from the data model. So, later, you'd see this level of automation for your own databases.

* __Customization and Debugging__ - this sample also includes customizations for extending the API and declaring logic, and how to use VSCode to debug these.  The Tutorial will clearly identify such pre-built customizations.

Now, [open the Tutorial](Tutorial.md).

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
