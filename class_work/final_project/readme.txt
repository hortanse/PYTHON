410.712.81
Advance Practical Computer Concepts for Bioinformatics

Final Project

Student name: Yi-Fan Chou

This project contains:

1. UNIX command

download and install SnpEff. Using 1000 genome project VCF file (for pratical perpose I used an example file in SnpEff package (chr22.vcf). It is smaller and easy to manage.

- input: test.chr22.vcf
- output: test.chr22.ann.vcf

2. using ipython notebook to generate sqlite3 database 

once generate the annotated VCF file, we can use pandas to read in the file and convert the data to sqlite3 database.

generate_database/final_project.ipynb
generate_database/final_project.html

database:
biopython.db

3. 
AJAX method: search_project.cgi, project.html, js/search.js, css/project.css
Jinja2 method: project_jinja2.cgi, project_search_jinja2.html, project_results_jinja2.html, project_jinja2.css




4. Challenge

I have hard time to displat my query results on the page. I wonder is AJAX problem, howevwe, I did similar as my unit08 hoemwork and it works on unit08.

Query results in notebook
please check on my final_project.html to see the query results.
We should able to see query results based on selected terms.

5. All the files can be found in jhu bfx server
/var/www/html/ychou7/final_project/

6. Please see my final_project.doc for summary.

Thank you!!
