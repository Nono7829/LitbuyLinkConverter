import requests
from urllib.parse import urlparse, parse_qs

INVITE_CODE = "0J4YBLOC5"

print("Générateur de liens Litbuy")
print("Ctrl + C pour quitter\n")

while True:
    url = input("Colle le lien Litbuy : ").strip()

    if not url:
        print("Lien vide.\n")
        continue

    try:
        response = requests.get(url, allow_redirects=True, timeout=10)
        final_url = response.url

        parsed = urlparse(final_url)
        query = parse_qs(parsed.query)

        product_id = query.get("id")
        channel = query.get("channel")

        if not product_id:
            print("Lien résolu mais ID produit introuvable.")
            print(f"[**CLICK HERE!**]({final_url})")
            continue

        product_id = product_id[0]
        channel_part = f"&channel={channel[0]}" if channel else ""

        new_link = (
            f"https://litbuy.com/products/details?"
            f"id={product_id}{channel_part}&inviteCode={INVITE_CODE}"
        )

        print("Lien généré :")
        print(new_link + "\n")

    except KeyboardInterrupt:
        print("\nArrêt du script.")
        break
    except Exception as e:
        print("Erreur :", e, "\n")
