# Item Catalog Project
This application showcases camera lenses for two different types of mounts in a
catalog. Each lens includes the full name, the type of mount, a picture of the
lens, a short description, as well as the retail price in USD. Anyone can freely
view the catalog, but users not logged in nor authorized may not edit nor delete
items that were not added themselves. In conclusion, this catalog utilizes
**CRUD**:

- **CREATE**: Logged in users can add new lenses to the catalog
- **READ**: Anyone can view all lenses in the catalog
- **UPDATE**: Authorized users can update their existing lenses in the catalog
- **DELETE**: Authorized users can delete their existing lenses in the catalog

## Files and Folders
* `database_setup.py` sets up required tables to be populated with items
* `lensinit.py` contains a small list of lenses and details to populate tables
* `project.py` is the actual application to run and brings everything together
* `client_secrets.json` contains required credentials to run Google sign-in
* `fb_client_secrets.json` contains required credentials to run Facebook sign-in
* `static folder` contains .css files for page styling
* `templates folder` contains .html webpage files for the catalog

## Dependencies
[Python 2.7](https://www.python.org/downloads/) must be installed.

The application runs on a virtual machine using [Vagrant](https://www.vagrantup.com/).

[VirtualBox](https://www.virtualbox.org/) is also required to properly run the
virtual machine.

To properly setup the virtual machine, Udacity's vagrant files from their [GitHub](https://github.com/udacity/fullstack-nanodegree-vm)
is required.

## Microsoft Windows Instructions
1. Place all project files and folders into the `vagrant\catalog` folder of the
Udacity vagrant package.  

2. Navigate to the vagrant directory and start a command prompt window; execute
`vagrant up`.

3. Once the process is completed, execute `vagrant ssh`.

4. Access the project files within vagrant by typing `cd /vagrant/catalog`.

5. Load the database tables by typing `python database_setup.py`.

6. Then populate the tables with `python lensinit.py`.

7. Finally, execute the project with `python project.py`.

8. Access the catalog from your browser with the URL `http://localhost:5000/`

9. **CRUD** all the lenses!

## Disclaimer
This application was written by Robert Nguyen with the help and guidance
of Udacity's Full Stack Web Developer Nanodegree Program.
