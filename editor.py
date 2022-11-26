import cv2
import os


def convert(loc, image_name, extension_convert_to, rename=None):
    image = cv2.imread(image_name)
    image_name_without_extension = image_name[:image_name.rfind(".")]
    #image_extension = image_name[image_name.rfind("."):]
    if (rename is not None):
        cv2.imwrite(os.path.join(
            loc, f"{rename}.{extension_convert_to}"), image)
        return
    cv2.imwrite(
        os.path.join(
            loc, f"{image_name_without_extension}.{extension_convert_to}"), image)


def resize_percent(loc, image_name, scale_percent, rename=None):
    image = cv2.imread(image_name)
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dsize = (width, height)
    resize = cv2.resize(image, dsize)

    if (rename is not None):
        cv2.imwrite(os.path.join(
            loc, f"{rename}"), resize)
        return

    cv2.imwrite(os.path.join(
        loc, f"{image_name}"), resize)


def resize(loc, image_name, with_input, height_input, rename=None):
    image = cv2.imread(image_name)
    width = with_input
    height = height_input
    dsize = (width, height)
    resize = cv2.resize(image, dsize)

    if (rename is not None):
        cv2.imwrite(os.path.join(
            loc, f"{rename}"), resize)
        return

    cv2.imwrite(os.path.join(
        loc, f"{image_name}"), resize)


def black_and_white(loc, image_name, rename=None):
    image = cv2.imread(image_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if (rename is not None):
        cv2.imwrite(os.path.join(
            loc, f"{rename}"), gray)
        return

    cv2.imwrite(os.path.join(
        loc, f"{image_name}"), gray)


def invert(loc, image_name, rename=None):
    image = cv2.imread(image_name)
    invert = cv2.bitwise_not(image)

    if (rename is not None):
        cv2.imwrite(os.path.join(
            loc, f"{rename}"), invert)
        return

    cv2.imwrite(os.path.join(
        loc, f"{image_name}"), invert)


def rotate(loc, image_name, angle_input, rename=None):
    image = cv2.imread(image_name)
    if (rename is not None):
        if (angle_input == "left"):
            angle = cv2.ROTATE_90_COUNTERCLOCKWISE
            rotated = cv2.rotate(image, angle)
            cv2.imwrite(os.path.join(
                loc, f"{rename}"), rotated)
        elif (angle_input == "right"):
            angle = cv2.ROTATE_90_CLOCKWISE
            rotated = cv2.rotate(image, angle)
            cv2.imwrite(os.path.join(
                loc, f"{rename}"), rotated)
        elif (angle_input == "flip-down"):
            angle = cv2.ROTATE_180
            rotated = cv2.rotate(image, angle)
            cv2.imwrite(os.path.join(
                loc, f"{rename}"), rotated)
        elif (angle_input == "flip-x"):
            flipped_horiz = cv2.flip(image, 1)
            cv2.imwrite(os.path.join(
                loc, f"{rename}"), flipped_horiz)
        elif (angle_input == "flip-down-x"):
            flipped_horiz = cv2.flip(image, -1)
            cv2.imwrite(os.path.join(
                loc, f"{rename}"), flipped_horiz)
        else:
            return
        return

    if (angle_input == "left"):
        angle = cv2.ROTATE_90_COUNTERCLOCKWISE
        rotated = cv2.rotate(image, angle)
        cv2.imwrite(os.path.join(
            loc, f"{image_name}"), rotated)
    elif (angle_input == "right"):
        angle = cv2.ROTATE_90_CLOCKWISE
        rotated = cv2.rotate(image, angle)
        cv2.imwrite(os.path.join(
            loc, f"{image_name}"), rotated)
    elif (angle_input == "flip-down"):
        angle = cv2.ROTATE_180
        rotated = cv2.rotate(image, angle)
        cv2.imwrite(os.path.join(
            loc, f"{image_name}"), rotated)
    elif (angle_input == "flip-x"):
        flipped_horiz = cv2.flip(image, 1)
        cv2.imwrite(os.path.join(
            loc, f"{image_name}"), flipped_horiz)
    elif (angle_input == "flip-down-x"):
        flipped_horiz = cv2.flip(image, -1)
        cv2.imwrite(os.path.join(
            loc, f"{image_name}"), flipped_horiz)
    else:
        return


def blur(loc, image_name, blur_number, rename=None):
    # ! Check of value is less than 0 and floot number
    if (blur_number < 0 or blur_number % 1 != 0):
        return
    image = cv2.imread(image_name)
    blur_image = cv2.GaussianBlur(image, (blur_number, blur_number), 0)

    if (rename is not None):
        cv2.imwrite(os.path.join(
            loc, f"{rename}"), blur_image)
        return
    cv2.imwrite(os.path.join(
        loc, f"{image_name}"), blur_image)


def pencilSketch(loc, image_name, rename=None):
    image = cv2.imread(image_name)
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert_img = cv2.bitwise_not(grey_img)
    blur_img = cv2.GaussianBlur(invert_img, (111, 111), 0)
    invblur_img = cv2.bitwise_not(blur_img)
    sketch_img = cv2.divide(grey_img, invblur_img, scale=256.0)

    if (rename is not None):
        cv2.imwrite(os.path.join(
            loc, f"{rename}"), sketch_img)
        return
    cv2.imwrite(os.path.join(
        loc, f"{image_name}"), sketch_img)
