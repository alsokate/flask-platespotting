from spot import plate
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        plate.debug = True

    plate.run(port=port)