  // ------- pagination ------

  // // Turn page selection into form submit
  // // q (and other?) parameters are in the form and will be submited? 
  // // document.on syntax required since this the markup was loaded by ajax.
  // $(document).on("click", "#source-paging", function(event){
  //   event.preventDefault();
  //   // get the page number from href
  //   var chosen_href = $(event.target).closest('li').children('a').attr('href');
  //   var href_split = chosen_href.split('=');  
  //   // page number = href_split[1]  
  //   // alert('in page nav. page num: ' + href_split[1]); 
  //   // set the page number in the hidden field
  //   $('#source-search-form').find('[type=hidden][name=page]').val(href_split[1])
  //   $('#source-search-form').submit()
  // });

  // // Turn page selection into form submit
  // // q (and other?) parameters are in the form and will be submited? 
  // // document.on syntax required since this the markup was loaded by ajax.
  // $(document).on("click", "#aaperson-paging", function(event){
  //   event.preventDefault();
  //   // get the page number from href
  //   var chosen_href = $(event.target).closest('li').children('a').attr('href');
  //   var href_split = chosen_href.split('=');  
  //   // page number = href_split[1]  
  //   // alert('in page nav. page num: ' + href_split[1]); 
  //   // set the page number in the hidden field
  //   $('#aaperson-search-form').find('[type=hidden][name=page]').val(href_split[1])
  //   $('#aaperson-search-form').submit()
  // });

  // Turn page selection into form submit
  // q (and other?) parameters are in the form and will be submited? 
  // document.on syntax required since this the markup was loaded by ajax.
  $(document).on("click", "#paging", function(event){
    console.log('got to plain pagine');
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
