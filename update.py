import os
import shutil


def update_text_resource(source_dir, dest_dir):
    dirs = os.listdir(dest_dir)
    string_file_name = "strings.xml"
    for dir_name in dirs:
        if dir_name.startswith("value"):
            source_path = source_dir + os.sep + dir_name + os.sep + string_file_name
            dest_path = dest_dir + os.sep + dir_name + os.sep + string_file_name
            print("try to copy [" + source_path + " to [" + dest_path + "]")
            shutil.copy(source_path, dest_path)


# def updateValueDir(sourceDir, destDir):
#

if __name__ == "__main__":
    update_text_resource("C:\\Develop\\work\\gitlab\\LifeUp-Private\\app\\src\\main\\res"
                         , "C:\\Develop\\LifeUp-Translation")
