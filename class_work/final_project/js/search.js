// this function executes our search via an AJAX call
function runSearch( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();

    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#gene_search').serialize();

    $.ajax({
	url: './search_project.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            $(*).css('cursor','default');
            processJSON(data);
        },
	error: function(jqXHR, textStatus, errorThrown){
            $(*).css('cursor','default');
            alert("Failed to perform gene search! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}


// this processes a passed JSON structure representing gene matches and draws it
//  to the result table
function processJSON( data ) {
    // set the span that lists the match count
    $('#match_count').text( data.match_count );

    // this will be used to keep track of row identifiers
    var next_row_num = 1;

    // iterate over each match and add a row to the result table for each
    $.each( data.matches, function(i, item) {
        var this_row_id = 'result_row_' + next_row_num++;

        // create a row and append it to the body of the table
        $('<tr/>', { "id" : this_row_id } ).appendTo('tbody');

        // add the chromosome column
        $('<td/>', { "text" : item.chromosome } ).appendTo('#' + this_row_id);

        // add the position column
        $('<td/>', { "text" : item.position } ).appendTo('#' + this_row_id);
		
		// add the id_snp column
        $('<td/>', { "text" : item.id_snp } ).appendTo('#' + this_row_id);

    });

    // now show the result section that was previously hidden
    $('#results').show();
}



// run our javascript once the page is ready
$(document).ready( function() {
    // define what should happen when a user clicks submit on our search form
    $('#submit').click( function() {
        $(*).css('cursor','default');
        runSearch();
        //return false;  // prevents 'normal' form submission
    });
});
