from flask import Blueprint, flash, redirect, render_template, request 


# internal imports
from rangers_shop.models import Product, db 
from rangers_shop.forms import ProductForm


# instantiate our Blueprint class

                                     # location of html files
site = Blueprint('site', __name__, template_folder='site_templates')


# use our site blueprint object to create our routes
@site.route('/')
def shop():
    
    # grab all of the products in our database via query
    allprods = Product.query.all() # same as SELECT * FROM products, list of objects from database 
    
    
    return render_template('shop.html', shop=allprods) # looking inside site_templates folder for a file called shop.html to render



@site.route('/shop/create', methods=['GET', 'POST'])
def create():
    
    #instantiate our ProductForm class
    
    createform = ProductForm()
    
    if request.method == 'POST' and createform.validate_on_submit():
        #graab our data
        name = createform.name.data
        image = createform.image.data
        description = createform.description.data
        price = createform.price.data 
        quantity = createform.quantity.data 
        
        product = Product(name, price, quantity, image, description) # instantiate our Product object from Product class
        
        
        db.session.add(product)
        db.session.commit()
        
        flash(f"You have successfully created product {name}", category='success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("We were unable to process your request", category='warning')
        return redirect('/shop/create')
    
    
    return render_template('create.html', form=createform)


@site.route('/shop/update/<product_id>', methods=['GET', 'POST'])
def update(product_id):
    # Grab our specific product based on the product_id 
    product = Product.query.get(product_id)
    
    # Instantiate our form 
    updateform = ProductForm()
    
    if request.method == 'POST' and updateform.validate_on_submit():
        # Update the product details
        product.name = updateform.name.data
        product.image = product.set_image(updateform.image.data, updateform.name.data)
        product.description = updateform.description.data
        product.price = updateform.price.data
        product.quantity = updateform.quantity.data 
        
        # Commit our changes
        db.session.commit()
        
        flash(f"You have successfully updated product {product.name}", category='success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("We were unable to process your request", category='warning')
        return redirect(f'/shop/update/{product.id}')
    
    # Render the update.html template with the form and product details
    return render_template('update.html', form=updateform, product=product)

    

@site.route('/shop/delete/<id>')
def delete(id):
    
    # query the databaase to find that product
    product = Product.query.get(id)
    
    db.session.delete(product)
    db.session.commit()
    
    return redirect('/')