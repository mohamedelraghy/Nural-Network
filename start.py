from GUI import GUI


def my_training_function():
    print("Training!")


def my_prediction_function():
    print("Prediticting")


def my_change_weights_function(weight):
    # this function should return the new changed weight
    print("Weight changed to " + weight)


def main():
    GUI(my_training_function, my_prediction_function, my_change_weights_function)


if __name__ == "__main__":
    main()
