# file_write_binary_mode.py

try:
    fw = open("my_bin_file.txt", 'wb')
    # 写入256字节,第一个字节为0x00, 第二个字节为0x01, ...
    # 第256个字正好是0xFF
    b = bytes(range(256))
    fw.write(b)

    fw.close()
except OSError:
    print("写文件失败!")