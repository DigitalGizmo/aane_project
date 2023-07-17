$(document).ready(function(){
// ------- pagination  ------

  // Turn page selection into form submit
  // q (and other?) parameters are in the form and will be submited? 
  // document.on syntax required since this the markup was loaded by ajax.
  $(document).on("click", "#paging", function(event){
    console.log('got to paging');
    // console.log('href: ' + $(event.target).closest('li').children('a').attr('href'));
    event.preventDefault();
    // get the page number from href
    var chosen_href = $(event.target).closest('li').children('a').attr('href');
    var href_split = chosen_href.split('=');  
    // page number = href_split[1]  
    // alert('in page nav. page num: ' + href_split[1]); 
    // set the page number in the hidden field
    $('#search-form').find('[type=hidden][name=page]').val(href_split[1])
    $('#search-form').submit()
  });

  // ------- SEARCH ------

  // click on checkbox submits form
  $('input[type="checkbox"]').change(function(event){
    console.log('got to checkbox change')
    // each time a new box is checked we should reset to page 1
    // (if nothing else there may not be a page 2 in new result)
    $('#search-form').find('[type=hidden][name=page]').val('1')
    $('#search-form').submit()   
  });

  // Zoom scroll to top -- possibly temporary
  $(document).on("click", ".to-top", function(event){
    console.log('got to go to top');
    event.preventDefault();
    document.getElementById('slimpop-container').scrollTo(0, 0);
    // get the page number from href
    // var chosen_href = $(event.target).closest('li').children('a').attr('href');
    // page number = href_split[1]  
    // alert('in page nav. page num: ' + href_split[1]); 
    // set the page number in the hidden field
  });

}); // end doc ready


