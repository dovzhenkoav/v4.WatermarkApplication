import cv2
import datetime as dt

class Brain():
    def __init__(self, main_image, watermark_type, watermark_text, watermark_image, position):
        self.main_image = main_image
        self.watermark_type = watermark_type
        self.watermark_text = watermark_text
        self.watermark_image = watermark_image
        self.position = position
        self.textsize = cv2.getTextSize(self.watermark_text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
        self.image = cv2.imread(self.main_image)



    def text_get_position(self, height, width):
        pos = self.position
        if pos == 'Top-Left':
            x = 5
            y = 30
        elif pos == 'Left':
            x = 5
            y = int(height/2 + 10)
        elif pos == 'Bottom-Left':
            x = 5
            y = height - 9

        elif pos == 'Top':
            x = int(width/2 - self.textsize[0]/2)
            y = 30
        elif pos == 'Center':
            x = int(width/2 - self.textsize[0]/2)
            y = int(height/2 + 10)
        elif pos == 'Bottom':
            x = int(width/2 - self.textsize[0]/2)
            y = height - 9

        elif pos == 'Top-Right':
            x = width - self.textsize[0] - 9
            y = 30
        elif pos == 'Right':
            x = width - self.textsize[0] - 9
            y = int(height/2 + 10)
        elif pos == 'Bottom-Right':
            x = width - self.textsize[0] - 9
            y = height - 9

        return (x, y)


    def img_get_position(self, h_img, w_img, h_wm, w_wm):
        pos = self.position

        if pos == 'Top-Left':
            top_y = 5
            bottom_y = top_y + h_wm
            left_x = 5
            right_x = left_x + w_wm
        elif pos == 'Left':
            center_y = int(h_img / 2)
            top_y = center_y - int(h_wm / 2)
            bottom_y = top_y + h_wm
            left_x = 5
            right_x = left_x + w_wm
        elif pos == 'Bottom-Left':
            bottom_y = h_img - 5
            top_y = bottom_y - h_wm
            left_x = 5
            right_x = left_x + w_wm

        elif pos == 'Top':
            center_x = int(w_img / 2)
            top_y = 5
            left_x = center_x - int(w_wm / 2)
            bottom_y = top_y + h_wm
            right_x = left_x + w_wm
        elif pos == 'Center':
            center_y = int(h_img / 2)
            center_x = int(w_img / 2)
            top_y = center_y - int(h_wm / 2)
            left_x = center_x - int(w_wm / 2)
            bottom_y = top_y + h_wm
            right_x = left_x + w_wm
        elif pos == 'Bottom':
            center_x = int(w_img / 2)
            bottom_y = h_img - 5
            top_y = bottom_y - h_wm
            left_x = center_x - int(w_wm / 2)
            right_x = left_x + w_wm

        elif pos == 'Top-Right':
            top_y = 5
            bottom_y = top_y + h_wm
            right_x = w_img - 5
            left_x = right_x - w_wm

        elif pos == 'Right':
            center_y = int(h_img / 2)
            top_y = center_y - int(h_wm / 2)
            bottom_y = top_y + h_wm
            right_x = w_img - 5
            left_x = right_x - w_wm
        elif pos == 'Bottom-Right':
            bottom_y = h_img - 5
            top_y = bottom_y - h_wm
            right_x = w_img - 5
            left_x = right_x - w_wm
        return top_y, bottom_y, left_x, right_x


    def get_magic(self):
        height, width, _ = self.image.shape
        if self.watermark_type == 'text':
            font = cv2.FONT_HERSHEY_SIMPLEX
            watermark_position = self.text_get_position(height, width)
            fontScale = 1
            fontColor = (255, 255, 255)
            thickness = 1
            lineType = 2

            cv2.putText(self.image, self.watermark_text,
                        watermark_position,
                        font,
                        fontScale,
                        fontColor,
                        thickness,
                        lineType)

        elif self.watermark_type == 'image':
            logo_img = cv2.imread(self.watermark_image)

            height, width, _ = self.image.shape
            wwm_height, wwm_width, _ = logo_img.shape

            wm_height = int(height/9)
            wm_width = int(wwm_width/(wwm_height/wm_height))
            wm_dim = (wm_width, wm_height)

            resized_wm = cv2.resize(logo_img, wm_dim, interpolation=cv2.INTER_AREA)

            h_img, w_img, _ = self.image.shape
            h_wm, w_wm, _ = resized_wm.shape

            top_y, bottom_y, left_x, right_x = self.img_get_position(h_img, w_img, h_wm, w_wm)


            roi = self.image[top_y:bottom_y, left_x:right_x]
            result = cv2.addWeighted(roi, 0.3, resized_wm, 1, 0)
            self.image[top_y:bottom_y, left_x:right_x] = result


    def get_preview(self):
        self.get_magic()
        cv2.namedWindow('Preview', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('Preview', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()











    def save_image(self):
        self.get_magic()
        today = dt.datetime.now()
        name = today.strftime("%Y-%m-%d--%H-%M-%S")
        cv2.imwrite(f".\output\{name}.jpg", self.image)