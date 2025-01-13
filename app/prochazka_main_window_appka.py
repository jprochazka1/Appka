### GUI imports
from guizero import *
from prochazka_main_appka import *

###GUI functions
def calculate_basic_user_data():
    try:
        fat_data['weight'] = round(float(optimal_fat_txtbox.value), 2)
        fat_data['skinfolds_sum'] = round(float(current_fat_txtbox.value), 2)
        calculate_fat_data()
        bmr_text.value = (
            f"\n       Without any activity,"
            f"\nyou should be able to consume up to:"
            f"\n{fat_data['cal_main_lvl']}kcal\nto "
            "preserve your current weight.       "
        )
    except:
        bmr_text.value = (
            "You must type a "
            "whole or decimal number\nin both fields."
        )
def health():
    zdravy = "Tvoje zdraví vypadá dobře, jen tak dál!"
    nezdravy = "Tvoje zdraví nevypadá dobře, koukej to napravit!"
    if psychical_health_slider.value > 50 or activity_cbox.value == True:
        bmr_text_2.value = f"{zdravy}"
    else:
        bmr_text_2.value = f"{nezdravy}"


    
###GUI App
app = App(layout="auto", title="Fat Burner", width=775, height=775)

##MAIN WINDOW
window1 = Box(app)

# Welcome text
welcome_text = Text(window1, text=(f"Welcome, user."))

# Calculate basic data
current_fat_header = Text(
    window1,
    text=(
        "        Please enter the sum"
        " of your three skinfold areas in milimeters (mm):"
    )
)
current_fat_txtbox = TextBox(window1)
optimal_fat_header = Text(
    window1,
    text=(f"Please enter your weight in kilograms (kg):")
)
optimal_fat_txtbox = TextBox(window1)
psychical_health_header = Text(
    window1,
    text=("On the scale of 10 to 100 how are you mentally healthy?")
)
psychical_health_slider = Slider(window1)
activity_header = Text(
    window1,
    text=("I am a physically active person")
)
activity_cbox = CheckBox(window1)
button = PushButton(
    window1,
    command=lambda: [calculate_basic_user_data(), health()],
    text="Calculate My Calorie Maintenance Level"
)

bmr_text = Text(window1, text="")
bmr_text_2 = Text(window1, text="")

# Display an image
image_widget = Picture(
    window1,
    image="resources/images/file.png",
    width=300,
    height=200,
    align="bottom"
)

app.display()
