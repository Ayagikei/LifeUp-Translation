import os
import shutil


def rename_translation_build_and_delete_unused(source_dir):
    dirs = os.listdir(source_dir)
    for dir_name in dirs:
        rename_values_dir(source_dir, dirs, dir_name)


def rename_values_dir(source_dir, dirs, dir_name):
    # dir_name has two "-"
    split = dir_name.split("-")
    if len(split) != 3:
        return
    if dir_name.startswith("values-"):
        file_size = getFileSize(source_dir + os.sep + dir_name)
        if file_size < 1024:
            # delete the file which is contain short translations
            shutil.rmtree(source_dir + os.sep + dir_name)
            return
        # get string between "-" and "-"
        language_code = dir_name.split("-")[1]
        # dis contains "values-en"
        if count_files(dirs, language_code) == 1:
            # rename file dir_name to "values" + langauge_code
            os.rename(dir_name, "values-" + language_code)

def count_files(dirs, language_code):
    count = 0
    for dir_name in dirs:
        if dir_name.startswith("values-" + language_code):
            count += 1
    return count

def getFileSize(filePath, size=0):
    for root, dirs, files in os.walk(filePath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
            print(f)
    return size

if __name__ == "__main__":
    rename_translation_build_and_delete_unused(os.getcwd())