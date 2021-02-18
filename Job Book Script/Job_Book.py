import os
import shutil

def main():
    #Create you list of job book folders
    job_book = ["A100_A200-Scope_Schedules", "A300-Cost", "A700-Safety", "D000-Design", \
        "D100-Drawings-IFC", "D200-Drawings-Asbuilt", "E200-Pressure Test Procedures", \
        "E300-Operating Procedures", "F100-Contractor Initiated Orders", "G100-Inspector Reports", \
        "G200-Pressure Test Documents", "G300-Welding Documentation", "G400-Materials", \
        "G700-Integrity Reports", "H100-Special Documents", "I100-General Documentation", \
        "I200-Waranties"]

    #Make a job book folder. Full path ensures you start in the correct directory
    os.chdir('C:/Users/parke/Desktop/Python_projects/Job_Book')

    #Create your job book folder
    try:
        os.mkdir('./job_book')
    except:
        print("Job book folder structure already exists")

    #Move into the newly created folder
    os.chdir('./job_book')

    #Make all your folder
    for entry in job_book:
        folder = entry
        try:
            os.mkdir(folder)
        except:
            print("individual folder " + folder + " already exists")

    #Move to you temp folder and list all the files
    os.chdir('../temp_files')

    #Scan the directory and return an iterative object to list the file
    files = os.scandir()
    for file in files:
        #Case for copying scope files: Design Basis Manuals, Xcel Schedules & Scope files
        if file.name.startswith('A1', 0, 2):
            shutil.copy('../temp_files/'+file.name,'../job_book/A100_A200-Scope_Schedules/'+file.name)

        #Case for copying safety files: JSA documents from Xcel contractors
        elif file.name.startswith('A7', 0, 2):
            shutil.copy('../temp_files/'+file.name,'../job_book/A700-Safety/'+file.name)
        
        #Case for copying engineering related files: EN calculations and spreadsheets
        elif file.name.startswith('D0', 0, 2):
            shutil.copy('../temp_files/'+file.name,'../job_book/D000-Design/'+file.name)
        
        #Case for copying engineering related files: EN IFC drawings
        elif file.name.startswith('D1', 0, 2):
            shutil.copy('../temp_files/'+file.name,'../job_book/D100-Drawings-IFC/'+file.name)

        #Case for copying engineering related files: EN As-built drawings
        elif file.name.startswith('D2', 0, 2):
            shutil.copy('../temp_files/'+file.name,'../job_book/D200-Drawings-Asbuilt/'+file.name)

        #Case for copying Xcel signed pressure test procedure
        elif file.name.startswith('E2', 0, 2):
            shutil.copy('../temp_files/'+file.name,'../job_book/E200-Pressure Test Procedures/'+file.name)

        #Case for copying Xcel signed tie-in procedure
        elif file.name.startswith('E3', 0, 2):
            shutil.copy('../temp_files/'+file.name,'../job_book/E300-Operating Procedures/'+file.name)     

        #Case for copying Procurement related documents: Bill of Ladings, Shipping Manifests, As-Built BOM
        elif file.name.startswith('F1', 0, 2):
            shutil.copy('../temp_files/'+file.name,'../job_book/F100-Contractor Initiated Orders/'+file.name)

        #Case for copying inspector site markups, redlines, and notes
        elif file.name.startswith('G1', 0, 2):
            shutil.copy('../temp_files/'+file.name,'../job_book/G100-Inspector Reports/'+file.name)

        #Case for copying pressure test logs, PITs pictures from pressure tests, and test related documents
        elif file.name.startswith('G2', 0, 2):
            shutil.copy('../temp_files/'+file.name,'../job_book/G200-Pressure Test Documents/'+file.name)      

        #Case for copying welding related documents, welder qualifications, NDE reports, etc.
        elif file.name.startswith('G3', 0, 2):
            shutil.copy('../temp_files/'+file.name,'../job_book/G300-Welding Documentation/'+file.name)   

        #Case for copying equipment related documents, MTRs, COCs, etc.
        elif file.name.startswith('G4', 0, 2):
            shutil.copy('../temp_files/'+file.name,'../job_book/G400-Materials/'+file.name)

        #Case for copying As-built site photos, 3 to 5 depending on the site
        elif file.name.startswith('H1', 0, 2):
            shutil.copy('../temp_files/'+file.name,'../job_book/H100-Special Documents/'+file.name)

        #Case for copying additional documents that don't fall under the previous categories
        elif file.name.startswith('I1', 0, 2):
            shutil.copy('../temp_files/'+file.name,'../job_book/I100-General Documentation/'+file.name)      

        else:
            print('The file ', file.name, ' does not match accepted job book categories. Review file name.')

    #Call scandir.close (optional)
    files.close()

main()