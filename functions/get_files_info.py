import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
        if os.path.commonpath([abs_working_dir, target_dir]) != abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        filelist = ""
        for item in os.listdir(target_dir):
            filename, fileformat = os.path.splitext(item)
            fullpath = os.path.join(target_dir, item)
            is_dir = os.path.isdir(fullpath)
            filesize = os.path.getsize(fullpath)
            if os.path.isfile(fullpath):
                filelist += f"- {filename}{fileformat}: file_size={filesize} bytes, is_dir={is_dir}\n"
            else:
                filelist += f"- {filename}: file_size={filesize} bytes, is_dir={is_dir}\n"
            
        return filelist
    except Exception as e:
        return f"Error: {e}"
