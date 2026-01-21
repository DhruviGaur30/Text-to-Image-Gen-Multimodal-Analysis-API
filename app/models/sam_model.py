class SamSegmenter:
    def segment(self, image):
        width, height = image.size

        # Fake regions just for pipeline integration
        regions = [
            {"id": 0, "box": (0, 0, width // 2, height // 2)},
            {"id": 1, "box": (width // 2, 0, width, height // 2)},
            {"id": 2, "box": (0, height // 2, width // 2, height)},
            {"id": 3, "box": (width // 2, height // 2, width, height)},
        ]

        return {
            "regions": regions,
            "image_size": (width, height),
        }
