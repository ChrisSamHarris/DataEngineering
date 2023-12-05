from invoke import task

# invoke --list 

@task
def build(c, clean=False):
    # invoke build --clean
    if clean:
        print("Cleaning!")
    print("Building!")
    
    
@task(help={'name': "Name of the person to say hi to."})
def hi(c, name):
    # invoke hi -n Chris 
    print("Hi {}!".format(name))
    
@task
def create_doc(c):
    c.run("""echo "Creating a new document, named 'new_doc.md'" """)
    c.run("touch new_doc.md")
    
    
# pre-requisite tasks
@task
def deletefolder(c):
    c.run("rm -rf invoke_example_folder")

@task(deletefolder)
def newfolder(c):
    c.run("mkdir invoke_example_folder")
