# بوت طلبات كافيه - ثناء | thanaa.codes

print("=" * 40)
print("☕ كافيه ثناء - اهلا فيك")
print("=" * 40)

print("\n✨ قائمة القهوة:")
print("1. قهوة عربية - 15 ريال")
print("2. اسبريسو - 18 ريال")
print("3. كابتشينو - 22 ريال")
print("4. لاتيه - 25 ريال")
print("5. موكا - 28 ريال")
print("6. قهوة مثلجة - 30 ريال")

choice = input("\nاختاري رقم القهوة: ")

drinks = {
    "1": ("قهوة عربية", 15),
    "2": ("اسبريسو", 18),
    "3": ("كابتشينو", 22),
    "4": ("لاتيه", 25),
    "5": ("موكا", 28),
    "6": ("قهوة مثلجة", 30),
}

drink_name, drink_price = drinks.get(choice, ("غير معروفة", 0))
print(f"\nاخترتي: {drink_name} - {drink_price} ريال")

print("\n📏 الحجم:")
print("1. صغير")
print("2. وسط - + 5 ريال")
print("3. كبير - + 10 ريال")

size_choice = input("اختاري الحجم: ")
sizes = {"1": ("صغير", 0), "2": ("وسط", 5), "3": ("كبير", 10)}
size_name, size_price = sizes.get(size_choice, ("وسط", 5))

print("\n🍰 تبي حلا معها؟")
print("1. لا، شكرا")
print("2. كوكيز - 12 ريال")
print("3. كيك عسل - 18 ريال")
print("4. تشيز كيك - 22 ريال")

sweet_choice = input("اختاري: ")
sweets = {"1": ("بدون حلا", 0), "2": ("كوكيز", 12), "3": ("كيك عسل", 18), "4": ("تشيز كيك", 22)}
sweet_name, sweet_price = sweets.get(sweet_choice, ("بدون حلا", 0))

qty = int(input("\nكم عدد الاكواب؟ "))
total = (drink_price + size_price) * qty + sweet_price

print("\n--- بيانات الطلب ---")
name = input("اسمك: ")
phone = input("رقم جوالك: ")

print("\n" + "=" * 40)
print("✅ تم استلام طلبك!")
print("=" * 40)
print(f"الاسم: {name}")
print(f"الجوال: {phone}")
print(f"الطلب: {drink_name}")
print(f"الحجم: {size_name}")
print(f"الحلا: {sweet_name}")
print(f"العدد: {qty}")
print(f"الاجمالي: {total} ريال")
print("\nطلبك بيجهز خلال 10 دقايق ☕💖")
print("=" * 40)
