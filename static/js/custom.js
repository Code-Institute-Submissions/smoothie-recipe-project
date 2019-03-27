
// function additional ingredients and method steps to be added on add recipe page 
        
$(document).ready(function() {
     
        var maxField = 10; //Input fields increment limitation
        var addButton = $('.add_button'); //Add button selector
        var addMethod = $('.add_method_button');
        var wrapper = $('.field_wrapper'); //Input field wrapper
        var insert_field = $('.method_field');
        var fieldHTML = '<div class="row"><div class="input-field field_wrapper col s12"><i class="material-icons prefix">local_grocery_store</i><input type="text" name="ingredients" value="" required/></div><a href="javascript:void(0);" class="remove_button validate"><i class="material-icons prefix">clear</i></a></div>'; //New input field html 
        var methodHTML = '<div class="row"><div class="input-field method_field col s12"><i class="material-icons prefix">description</i><input name="method" id="method" type="text" class="validate" required/><label for="icon_prefix">Method</label></div><a href="javascript:void(0);" class="remove_button validate"><i class="material-icons prefix">clear</i></a></div>';
        var x = 1; //Initial field counter is 1
    
            //Once add button is clicked
            $(addButton).click(function(){
                //Check maximum number of input fields
                if(x < maxField){ 
                    x++; //Increment field counter
                    $(wrapper).append(fieldHTML); //Add field html
                }
            });
            $(addMethod).click(function(){
                if(x < maxField){
                    x++;
                    $(insert_field).append(methodHTML);
                }
            });

            //Once remove button is clicked
            $(wrapper).on('click', '.remove_button', function(e){
            e.preventDefault();
            $(this).parent('div').remove(); //Remove field html
            x--; //Decrement field counter
    });
            $(insert_field).on('click', '.remove_button', function(e){
            e.preventDefault();
            $(this).parent('div').remove(); //Remove field html
            x--; //Decrement field counter
    });
});