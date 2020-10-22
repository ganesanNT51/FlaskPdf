$( document ).ready(function() {
    // alert('in jquery');

    $("#alert-danger").hide();
    $("#alert-success").hide();

    getSignupindex();

    signup_validation();


    // $("#cust").submit(function()
    // {
    //     alert('test');
    //     return false;
    // })

    $("#signup_next").click(function()
    {

        signup_validation();
        if($("#signup").valid())
        {
            alert("valid")


            $.ajax({
                      type: 'POST', // <-- get method of form
                      url: $("#signup").attr('action'), // <-- get action of form
                      data: $("#signup").serialize(), // <-- serialize all fields into a string that is ready to be posted to your PHP file
                      dataType: 'json',
                      // beforeSend: function(){
                      // },
                      success: function(data){
                        if(data.status == 1)
                        {
                            $("#alert-success").show();
                            $("#alert-success").html(data.message);
                            // $("#myindexhtml").html(data.html);
                            // window.location.replace("http://127.0.0.1:5000/cust_index");

                            // alert(data.message);
                        }
                        else
                        {
                            $("#alert-danger").show();
                            $("#alert-danger").html(data.message)
                           // alert(data.message);
                        }
                        },
                        error: function(XMLHttpRequest, textStatus, errorThrown) { 
                          //location.reload();  
                        }                      
              });   


        }
        // else
        // {
        //     alert("in valid")
        // }
        // return true;

         // alert("test")

         // $("#alert-danger").hide();
         // $("#alert-success").hide();


         
        
        return false;
    })



    $("#mytest").click(function()
    {

         alert("test")

          // result =  cus_ajax("http://127.0.0.1:5000/mytest_ajax","GET",{'name':'test'},'json');



         $.ajax({
                      type: 'GET', // <-- get method of form
                      url: "http://127.0.0.1:5000/mytest_ajax", // <-- get action of form
                      data: {'name':'test'}, // <-- serialize all fields into a string that is ready to be posted to your PHP file
                      dataType: 'json',
                      // beforeSend: function(){
                      // },
                      success: function(data){
                        if(data.status == 1)
                        {
                            alert(data.message);
                        }
                        else
                        {
                           alert(data.message);
                        }
                        },
                        error: function(XMLHttpRequest, textStatus, errorThrown) { 
                          //location.reload();  
                        }                      
              });   
        
        return false;
    })




});


function getSignupindex() {
    // result =  cus_ajax("GET","http://127.0.0.1:5000/contact_index_ajax","","json");


         $.ajax({
                      type: 'GET', // <-- get method of form
                      url: "http://127.0.0.1:5000/contact_index_ajax", // <-- get action of form
                      // data: {'name':'test'}, // <-- serialize all fields into a string that is ready to be posted to your PHP file
                      dataType: 'json',
                      // beforeSend: function(){
                      // },
                      success: function(data){
                        if(data.status == 1)
                        {
                           $("#myindexhtml").html(data.html);
                        }
                                                },
                        error: function(XMLHttpRequest, textStatus, errorThrown) { 
                          //location.reload();  
                        }                      
              });   


}

function signup_validation() {

     errorClass: 'errors',
    $("#signup").validate({
        rules: {
            mobile: "required",
            name: "required",
        },

        messages: {
            
            prcontact_numberefix : "Please enter the contact number",
            name : "Please enter the name"
            
        },

        highlight: function(element) {
            $(element).parent().addClass('error')
        },
    
        unhighlight: function(element) {
            $(element).parent().removeClass('error')
        },

        submitHandler: function(form) {
            form.submit();
        }
    });
}


function cus_ajax(type,url,data,dataType) {
     $.ajax({
                      type: type, // <-- get method of form
                      url: url, // <-- get action of form
                      data:data , // <-- serialize all fields into a string that is ready to be posted to your PHP file
                      dataType: dataType,
                      async:true,
                      // beforeSend: function(){
                      // },
                      success: function(data){
                        return data;
                      },
                      error: function(XMLHttpRequest, textStatus, errorThrown) { 
                          //location.reload();  
                          return "";
                      }                      
              });   
}

