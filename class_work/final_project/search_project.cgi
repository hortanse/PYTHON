#!/usr/local/bin/python3

import cgi, json
import os
import sqlite3

def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    chrom = form.getvalue('chrom')
    term1 = form.getvalue('search_term1')
    term2 = form.getvalue('search_term2')
    #chrom = 22
    #term1 = 'downstream_gene_variant'
    #term2 = 'MODIFIER'    


    conn = sqlite3.connect('biopython.db')
    curs = conn.cursor()

    query = '''
        SELECT CHROM, POS, ID 
           FROM chromosome
        WHERE CHROM = ? AND INFO LIKE ? AND INFO LIKE ? 
    '''
    curs.execute(query, (chrom, '%' + term1 + '%', '%' + term2 +'%' ))

    results = { 'match_count': 0, 'matches': list() }
    i = 5
    for (CHROM, POS, ID) in curs:
        i -= 1
        if i < 0:
            break
        results['matches'].append({'chromosome': CHROM, 'position': POS, 'id_snp':ID})
        results['match_count'] += 1
        
    conn.commit()
    curs.close()
    conn.close()

    print(json.dumps(results))


if __name__ == '__main__':
    main()

