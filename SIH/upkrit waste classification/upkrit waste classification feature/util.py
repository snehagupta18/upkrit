import tensorflow as tf
import numpy as np

model = None
output_class = ["Batteries", "Clothes", "E-waste", "Glass", "Light Blubs", "Metal", "Organic", "Paper", "Plastic"]
data = {
"Batteries":
	["Battery recycling is important because it helps prevent pollution, conserves valuable resources, and reduces the energy-intensive production of new batteries.<br><br><br><strong>What can we do ?</strong><br><br>• Participate in battery collection programs provided by local recycling centers or electronics retailers<br>"
    "• Use rechargeable batteries whenever possible to extend their lifespan and reduce waste<br><br>"
    "• Locate nearby drop-off locations for safe battery disposal and recycling<br><br>"
    "• Spread awareness about the importance of battery recycling to encourage responsible disposal practices<br><br>",
	"U6lswfrIoFM", "T-J50nsk-OI"],
"Clothes":
	["Clothes recycling is important because it reduces textile waste, conserves resources, and minimizes the environmental impact of the fashion industry.<br><br><br><strong>What can we do ?</strong><br><br>• Donate gently-used clothing to local charities or thrift stores for reuse.<br><br>"
    "• Participate in clothing swap events to exchange clothes with others.<br><br>"
    "• Recycle old and worn-out textiles by dropping them off at designated collection points.<br><br>"
    "• Purchase sustainable and eco-friendly clothing made from recycled materials.<br><br>",
	"Bhi7S06pwv4", "7i0QMnz4ExY"],
"E-waste":
	["E-Waste recycling is important because it prevents hazardous materials from contaminating the environment, conserves valuable resources, and reduces electronic waste in landfills.<br><br><br><strong>What can we do ?</strong><br><br>•Take old electronics to authorized e-waste recycling centers or events.<br><br>"
    "• Donate working electronic devices to organizations or individuals in need.<br><br>"
    "• Trade in or recycle mobile phones, tablets, and laptops through manufacturer or retailer programs.<br><br>"
    "• Educate yourself and others about responsible e-waste disposal practices to promote recycling awareness.<br><br>",
	"eT34ypRodB0","S2lmPIa1iWE"],
"Glass":
	["Glass recycling is important because it conserves energy, reduces greenhouse gas emissions, and decreases the need for raw materials in glass production.<br><br><br><strong>What can we do ?</strong><br><br>• Separate glass bottles and jars from other recyclables to ensure proper recycling.<br><br>"
    "• Deposit glass containers in designated recycling bins or collection points.<br><br>"
    "• Support local glass recycling programs and initiatives.<br><br>"
    "• Promote the use of glass products made from recycled glass to close the recycling loop.<br><br>",
	"ZEVq0oxL4_A", "dIOTsBhFF7M"],
"Light Blubs":
	["Light bulb recycling is important because it prevents the release of hazardous materials, conserves energy, and reduces waste in landfills.<br><br><br><strong>What can we do ?</strong><br><br>• Dispose of compact fluorescent lamps (CFLs) and fluorescent tubes at designated hazardous waste collection sites.<br><br>"
    "• Recycle incandescent bulbs through local household hazardous waste programs, if available.<br><br>"
    "• Consider switching to energy-efficient LED bulbs, which last longer and require less frequent disposal.<br><br>"
    "• Educate yourself and others about proper light bulb disposal methods to ensure safe recycling.<br><br>",
	"K1VL_LOAkrg", "v67xq3pm0y8"],
"Metal":
	["Metal recycling is important because it conserves natural resources, reduces energy consumption, and minimizes the environmental impact of mining and production.<br><br><br><strong>What can we do ?</strong><br><br>• Separate metal items such as aluminum cans and steel containers from your regular waste for recycling.<br><br>"
    "• Take scrap metal to local recycling centers or scrap yards for proper disposal and recycling.<br><br>"
    "• Support recycling initiatives that promote the collection and reuse of metal materials.<br><br>"
    "• Choose products made from recycled metal to encourage the demand for sustainable materials.<br><br>",
	"KmMP67eC2tg", "LyR7I5xsK9k"],
"Organic":
	["Organic waste recycling is important because it reduces methane emissions from landfills, enriches soil health, and conserves resources through composting.<br><br><br><strong>What can we do ?</strong><br><br>• Compost kitchen scraps like fruit and vegetable peels, coffee grounds, and eggshells in a backyard compost bin or pile.<br><br>"
    "• Use a composting service if available in your area to process organic waste into valuable compost.<br><br>"
    "• Support community composting programs and encourage local composting initiatives.<br><br>"
    "• Educate yourself and others about the benefits of composting and how to properly manage organic waste.<br><br>",
	"gg4TSqH7pnw", "r7wgIG-0-Zw"],
"Paper":
	["Paper recycling is important because it conserves trees, reduces energy consumption, and minimizes water usage and pollution associated with paper production.<br><br><br><strong>What can we do ?</strong><br><br>• Separate paper and cardboard materials from your regular trash for recycling.<br><br>"
    "• Use both sides of paper when printing or writing to reduce paper waste.<br><br>"
    "• Support paper recycling programs in your community or workplace.<br><br>"
    "• Choose products made from recycled paper to promote sustainable paper production.<br><br>",
	"HmhPuIKw0HY", "20QuJf4vbGk"],
"Plastic":
	["Plastic recycling is important because it reduces plastic pollution, conserves resources, and decreases the environmental impact of plastic production and disposal.<br><br><br><strong>What can we do ?</strong><br><br> • Sort plastic containers and packaging by their recycling codes, and place them in the appropriate recycling bins.<br><br>"
    "• Reduce single-use plastic consumption by using reusable alternatives such as water bottles, bags, and containers.<br><br>"
    "• Support local recycling programs and initiatives aimed at collecting and processing plastic waste.<br><br>"
    "• Choose products made from recycled plastics to promote a circular economy and reduce the demand for new plastic production.<br><br>",
	"rYwBL_6hB2I", "fYFkDnN8IIo"]
}


def load_artifacts():
    global model
    model = tf.keras.models.load_model("classifyWaste.h5" , compile = False)
   

def classify_waste(image_path):
	global model, output_class
	test_image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
	test_image = tf.keras.preprocessing.image.img_to_array(test_image) / 255
	test_image = np.expand_dims(test_image, axis = 0)
	predicted_array = model.predict(test_image)
	predicted_value = output_class[np.argmax(predicted_array)]
	return predicted_value, data[predicted_value][0], data[predicted_value][1], data[predicted_value][2]

