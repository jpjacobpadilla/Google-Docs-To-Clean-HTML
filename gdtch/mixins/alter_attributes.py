from pathlib import Path
import random


class AlterAttributes:
    def give_images_unique_names(self) -> None:
        """
        Attempts to create a better (or at least unique) image name than the
        default which is just a number.
        """
        for i, element in enumerate(self.elements):
            if element.tag == 'img':
                original_src = Path(element.attrib['src'])
                image_subject = self._find_subject(i)

                new_src = original_src.with_stem(f'{image_subject}-{random.randint(100_000_000, 999_999_999)}')

                element.attrib['src'] = new_src.as_posix()
                self._update_image_name(original_src, new_src)

    def _update_image_name(self, original: Path, new: Path) -> None:
        root_dir = Path(self.html_file_path).parent

        full_original_path = root_dir.joinpath(original)
        full_new_path = root_dir.joinpath(new)

        full_original_path.rename(full_new_path)

    def _find_subject(self, element_index: int) -> str:
        for i in range(element_index, -1, -1):
            element = self.elements[i]
            if element.tag.startswith('h') and element.tag[-1].isnumeric():
                return '-'.join(element.text.lower().split())

