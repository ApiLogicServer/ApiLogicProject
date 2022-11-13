# Quick Start

<details markdown>

<summary>What is API Logic Server</summary>

&nbsp;

API Logic Server creates __customizable database web app projects:__

* __Creation is Instant:__ create projects with a single command

* __Projects are Highly Functional,__ providing:

    * __API:__ an endpoint for each table, with filtering, sorting, pagination and related data access

    * __Admin UI:__ multi-page / multi-table apps, with page navigations, automatic joins and declarative hide/show

* __Projects are Customizable, using _your IDE_:__ such as VSCode, PyCharm, etc, for familiar edit/debug services

* __Business Logic Automation:__ using unique spreadsheet-like rules, extensible with Python :trophy:

&nbsp;

<details markdown>

<summary>Why Does It Matter: Faster, Simpler, Modern Architecture</summary>

&nbsp;

<summary>Why Does It Matter: Faster, Simpler, Modern Architecture</summary>

Automation makes it __faster:__ what used to require weeks or months is now immediate.  Unblock UI Dev, and engage business users - _early_ - instead of investing in a misunderstanding.

Automation makes it __simpler:__ this reduces the risk of architectural errors, e.g., APIs without pagination.

Automation guarantees a __modern software architecture:__ _container-ready_, _API-based_, with _shared logic_ between UIs and APIs (no more logic in UI controllers), in a predictable structure for maintenance.

</details>


</details>

</details>

&nbsp;

## 1. Open in Codespaces (Done)

Open [this template project](https://github.com/ApiLogicServer/ApiLogicProject) in Codespaces.

<details markdown>

<summary>Show Me How</summary>

&nbsp;

<figure><img src="https://github.com/valhuber/apilogicserver/wiki/images/git-codespaces/open-on-codespaces.jpg?raw=true"></figure>

&nbsp;

__1. Use your GitHub account__ - no additional sign-up required

__2. Load the working_software_now project from GitHub__

To access this GitHub project with Codespaces

1. __Open [this page](https://github.com/ApiLogicServer/working_software_now)  _in a new window___, and 
2. Click __Open > Codespaces__ as shown below
3. You will see an empty project.

These instructions will continue in Codespaces.

<details markdown>

&nbsp;

<summary>What Is Happening</summary>

You will now see the template project - open in VSCode, _in the Browser._  But that's just what you _see..._

Behind the scenes, Codespaces has requisitioned a cloud machine, and loaded the template - with a _complete development environment_ - Python, your dependencies, git, etc.  

You are attached to this machine in your Browser, running VSCode.

These instructions are now visible in VS Code, to minimize window switching.

> :trophy: Pretty remarkable.

</details>

</details>


&nbsp;

## 2. Create a project _(Start Here)_

Paste this into the Terminal window (lower right):

```
ApiLogicServer create --project_name=./ --db_url=
```

When prompted, _do **not** rebuild the container._

<details markdown>

<summary>What Is Happening</summary>

&nbsp;

This is **not** a coded application.

The system examined your database (here, the default), and __created an _executable project:___

* __API__ - an endpoint for each table, with full CRUD services, filtering, sorting, pagination and related data access

* __Admin UI__ - multi-page / multi-table apps, with page navigations and automatic joins

__Projects are Customizable, using _your IDE_:__ the Project Explorer shows the project structure.  Use the code editor to customize your project, and the debugger to debug it.

__Business Logic is Automated:__ use unique spreadsheet-like rules to declare multi-table derivations and constraints - 40X more concise than code.  Extend logic with Python.


<details markdown>

<summary>Using your own database</summary>

&nbsp;

In this case, we used a default Customers/Orders database.  To use your own database, provide the `db_url` [like this](../Database-Connectivity/).

</details>
</details>

&nbsp;

## 3. Start Server, Admin App

The project is ready to run.

Use the prebuilt Run Configuration to start the server, and the prebuilt Port to start the web app.

<details markdown>

<summary>Show Me How</summary>

As shown below:

1. Use the default __Run Configuration__ to start the server, and 

2. Click __Ports > Globe__ to start the web app. 

<figure><img src="https://github.com/valhuber/apilogicserver/wiki/images/git-codespaces/create-port-launch-simple.jpg?raw=true"></figure>

</details>
&nbsp;

## 4. Explore the Tutorial

[Open the Tutorial](Tutorial.md) to explore the sample project.

<details markdown>

&nbsp;

<summary>Tutorial Overview</summary>

The Tutorial will enable you to explore 2 key aspects:

* __Initial Automation__ - API and UI creation are automated from the data model. So, later, you'd see this level of automation for your own databases.

* __Customization and Debugging__ - this sample also includes customizations for extending the API and declaring logic, and how to use VSCode to debug these.  The Tutorial will clearly identify such pre-built customizations.

</details>

&nbsp;

Extensive [product documentation is available here](https://valhuber.github.io/ApiLogicServer/) - checkout the [FAQs](https://valhuber.github.io/ApiLogicServer/FAQ-Frameworks/).

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

API Logic Server is an open source Python project.  It runs as a standard Python (`pip`) install, or under Docker. It consists of:

* a set of runtimes (api, user interface, data access) for project execution, plus

* a CLI (Command Language Interface) to create executable projects with a single command

   * Customize your projects in an IDE such as VSCode or PyCharm


> :bulb: API Logic Server reads your schema, and creates an executable, customizable project.

&nbsp;

# Appendices

Here is some background about API Logic Server.


&nbsp;&nbsp;

## Project Information

| About                    | Info                               |
|:-------------------------|:-----------------------------------|
| Created                  | Nov 7, 2022 07:24:31                      |
| API Logic Server Version | 6.02.35           |
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
