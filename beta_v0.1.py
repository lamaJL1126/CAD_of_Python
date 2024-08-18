import ezdxf

print("""
           
       _ - D - _
  A_ -     .     - _     
  |- _     .         - _ 
  |    - _ .         _ - C
  |        - _   _ -     |
  |        .   B         |
  |        .   |         |
  |    _ - H - |         |
  |_ -         | - _     |
  E- _         |     - _ |
       - _     |     _ - G
           - _ | _ -     
               F
""")


import ezdxf

def create_cube_dxf(filename, points):
    # 創建一個新的 DXF 文件
    doc = ezdxf.new()
    msp = doc.modelspace()
    
    # 確保有 8 個點
    if len(points) != 8:
        raise ValueError("需要 8 個三維點來生成立方體")

    # 定義立方體的邊
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # 底面邊
        (4, 5), (5, 6), (6, 7), (7, 4),  # 上面邊
        (0, 4), (1, 5), (2, 6), (3, 7)   # 垂直邊
    ]

    # 畫出立方體的邊
    for start_idx, end_idx in edges:
        start_point = points[start_idx]
        end_point = points[end_idx]
        msp.add_line(start_point, end_point)
    
    # 儲存 DXF 檔案
    doc.saveas(filename)

# 輸入八個三維點
points = []
for i in range(1, 9):
    x = float(input(f"輸入第 {i} 個點的 X 坐標: "))
    y = float(input(f"輸入第 {i} 個點的 Y 坐標: "))
    z = float(input(f"輸入第 {i} 個點的 Z 坐標: "))
    points.append((x, y, z))

# 創建 DXF 文件
create_cube_dxf("cube.dxf", points)
print("立方體 CAD 檔案已生成: cube.dxf")