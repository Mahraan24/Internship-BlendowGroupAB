import cv2

img = cv2.imread("Images/img_ui.png")

regions = [
    # y1, y2, x1, x2
    (340, 360, 55, 480),  # title
    (492, 906, 54, 840),  # document text
]

def redact(region, text, font_scale):
    y1, y2, x1, x2 = region
    img[y1:y2, x1:x2] = (40, 40, 40)
    font = cv2.FONT_HERSHEY_SIMPLEX
    size, _ = cv2.getTextSize(text, font, font_scale, 1)
    text_x = x1 + (x2 - x1 - size[0]) // 2
    text_y = y1 + (y2 - y1 + size[1]) // 2

    cv2.putText(
        img, text, (text_x, text_y),
        font, font_scale, (255, 255, 255), 1, cv2.LINE_AA
    )

redact(regions[0],"[REDACTED]",0.5)
redact(regions[1],"[LEGAL TEXT REDACTED]",1.0)

# cv2.imwrite("Images/img_ui_redacted.png", img)
cv2.imwrite("Images/img_ui.png", img)