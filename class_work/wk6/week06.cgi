#!/usr/local/bin/python3
import cgi
import mysql.connector
import jinja2

# This line tells the template loader where to search for template files
templateLoader = jinja2.FileSystemLoader( searchpath="./" )

# This creates your environment and loads a specific template
env = jinja2.Environment(loader=templateLoader)
template = env.get_template('week06.html')

form = cgi.FieldStorage()
gene_name = form.getvalue('gene_in')
#gene_name = 'bifunctional'
gene_name = str(gene_name)

conn = mysql.connector.connect(user='ychou7', password='$Nat0820Brad1028$',
                                  host='localhost', database='ychou7_chado')
curs = conn.cursor()

qry = """SELECT f.uniquename, product.value
           FROM feature f
           JOIN cvterm polypeptide ON f.type_id=polypeptide.cvterm_id
           JOIN featureprop product ON f.feature_id=product.feature_id
           JOIN cvterm productprop ON product.type_id=productprop.cvterm_id
           WHERE polypeptide.name = 'polypeptide'
           AND productprop.name  = 'gene_product_name'
           AND product.value LIKE %s"""
curs.execute(qry, ("%" + gene_name + "%",))

genes_table = list()
for row in curs:
    genes_table.append(row)

print("Content-Type: text/html\n\n")
print(template.render(genes = genes_table))

conn.commit()
curs.close()
conn.close()

