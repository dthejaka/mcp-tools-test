
import httpx
# from dinero import Dinero
# from dinero.currencies import AUD

async def shopify_search(store_domain, access_token, search_query, count=20, include_description = False):
    print('SHOPIFY')
    # Set the API endpoint for the Storefront API
    url = f'https://{store_domain}/api/2024-10/graphql.json'

    # Define the GraphQL query to get products
    query = '''
    {
      search(query: "%s", first: %s, types: PRODUCT) {
        edges {
          node {
            ... on Product {
              id
              title
              descriptionHtml
              vendor
              onlineStoreUrl
              featuredImage {
                id
                url(transform: { preferredContentType: PNG })
                altText
              }
              priceRange {
                minVariantPrice {
                  amount
                  currencyCode
                }
              }
              metafield(namespace: "custom", key: "MPN") {
                value
              }
            }
          }
        }
      }
    }
    ''' % (search_query, count)

    # Set the headers for the request
    headers = {
        'X-Shopify-Storefront-Access-Token': access_token,
        'Content-Type': 'application/json',
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json={'query': query}, headers=headers)

        if response.status_code == 200:
            print('akkkkkkkkkkkkk')
            products = response.json()
        else:
            products = []

    #
    print('alllllllllll')
    product_list = []
    if products:
        products = products['data']['search']['edges']
        for product in products:
            product = product['node']
            try:
                print(787878)
                # print(product)
                # amount = Dinero(product['priceRange']['minVariantPrice']['amount'], AUD)
                amount = product['priceRange']['minVariantPrice']['amount']
                if include_description:
                    description = product['descriptionHtml']
                    # print(99, description)
                else:
                    description = ''
                product_list.append({
                    "sku": str(product['id'].split('/')[-1]),
                    "title": str(product['title']),
                    "price": str(amount.format(symbol=True)),
                    "description": str(description),
                    "url": str(product['onlineStoreUrl']),
                    "imageUrl": str(product['featuredImage']['url']),
                })
                print('extracted')
            except:
                amount = product['priceRange']['minVariantPrice']['amount']
                if include_description:
                    description = product.get('descriptionHtml', '')
                else:
                    description = ''
                product_list.append({
                    "sku": str(product.get('id', '').split('/')[-1]),
                    "title": str(product.get('title', '')),
                    "price": str(amount.format(symbol=True)),
                    "description": str(description),
                    "url": str(product.get('onlineStoreUrl', '')),
                    "imageUrl": str(product.get('featuredImage', {}).get('url', '')),
                })
    else:
        pass

    return product_list

