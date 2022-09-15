def add_cart(request,product_id):
#      product=Product.objects.get(id=product_id)
#      try:
#           cart=Cart.objects.get(cart_id=_cart_id(request))
#      except ObjectDoesNotExist:
#           cart=Cart.objects.create(cart_id=_cart_id(request))
#           cart.save()
#      try:
#           cart_item=CartItem.objects.get(product=product,cart=cart)
            if cart_item.quantity < cart_item.product.stock:
               if request.method == 'POST':
               quantity = request.POST['quantity']
               cart_item.quantity += int(quantity)
#           cart_item.quantity +=1
#           cart_item.save()
#      except Cart.DoesNotExist:
#           cart_item=CartItem.objects.create(product=product,quantity=1,cart=cart)
#           cart_item.save()
#      return redirect('cart:cart_detail')
