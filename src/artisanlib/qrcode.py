#

import qrcode # type: ignore
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from qrcode.main import QRCode # type: ignore # pylint: disable=unused-import

try:
    from PyQt6.QtGui import QImage, QPixmap,QPainter # @UnusedImport @Reimport  @UnresolvedImport
    from PyQt6.QtCore import Qt # @UnusedImport @Reimport  @UnresolvedImport
except ImportError:
    from PyQt5.QtGui import QImage, QPixmap,QPainter # type: ignore # @UnusedImport @Reimport  @UnresolvedImport
    from PyQt5.QtCore import Qt # type: ignore # @UnusedImport @Reimport  @UnresolvedImport

##########################################################################
#####################     QR Image   #####################################
##########################################################################

class QRImage(qrcode.image.base.BaseImage): # type: ignore # pyright: "base" is not a known member of module "qrcode.image"

    def new_image(self, **_kwargs):
        img = QImage(self.pixel_size, self.pixel_size, QImage.Format.Format_RGB16)
        img.fill(Qt.GlobalColor.white)
        return img

    def pixmap(self):
        return QPixmap.fromImage(self.get_image())

    def drawrect(self, row, col):
        painter = QPainter(self.get_image())
        painter.fillRect(
            (col + self.border) * self.box_size,
            (row + self.border) * self.box_size,
            self.box_size, self.box_size,
            Qt.GlobalColor.black)

    def save(self, stream, kind=None):
        pass

    def process(self):
        pass

    def drawrect_context(self, row: int, col: int, qr: 'QRCode') -> None:
        pass

def QRlabel(url_str):
    qr = qrcode.QRCode(
        version=None, # 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L, # type:ignore # pyright: "constants" is not a known member of module "qrcode"
        box_size=4,
        border=1,
        image_factory=QRImage)
    qr.add_data(url_str)
    qr.make(fit=True)
    return qr
