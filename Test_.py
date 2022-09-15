import xlrd
import xlwt
import math

# 注：油箱 1 输送给油箱 2，油箱 6 输送给油箱 5，油箱 2，3，4，5 燃烧燃料
record_cal = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# xyz 和 zbc 都以 m 为单位
box1_xyz = [8.91304348, 1.20652174, 0.61669004]
box2_xyz = [6.91304348, -1.39347826, 0.21669004]
box3_xyz = [-1.68695652, 1.20652174, -0.28330996]
box4_xyz = [3.11304348, 0.60652174, -0.18330996]
box5_xyz = [-5.28695652, -0.29347826, 0.41669004]
box6_xyz = [-2.08695652, -1.49347826, 0.21669004]
box_xyzs = [box1_xyz, box2_xyz, box3_xyz, box4_xyz, box5_xyz, box6_xyz]
box1_abc = [1.5, 0.9, 0.3]
box2_abc = [2.2, 0.8, 1.1]
box3_abc = [2.4, 1.1, 0.9]
box4_abc = [1.7, 1.3, 1.2]
box5_abc = [2.4, 1.2, 1]
box6_abc = [2.4, 1, 0.5]
box_abcs = [box1_abc, box2_abc, box3_abc, box4_abc, box5_abc, box6_abc]
box_xyz0s = []

for j in range(6):
    box_abc = box_abcs[j]
    box_xyz = box_xyzs[j]
    box_x0 = box_xyz[0] - 0.5 * box_abc[0]
    box_y0 = box_xyz[1] - 0.5 * box_abc[1]
    box_z0 = box_xyz[2] - 0.5 * box_abc[2]
    box_xyz0s.append([box_x0, box_y0, box_z0])
planet_m0 = 3000  # kg
ru = 850  # kg/m^3
box_vs = [0.3, 1.5, 2.1, 1.9, 2.6, 0.8]  # m^3
box_ms = []
for i in range(6):
    box_ms.append(box_vs[i] * ru)
box_mass_centers = [[], [], [], [], [], []]


def calMassCenterOfSingleBox(h, theta, a, b, c):
    print('tan_theta:' + str(math.tan(abs(((theta / 180) * math.pi)))))
    if theta == 0:  # 矩形
        print('矩形')
        record_cal[0] = record_cal[0] + 1
        return [a / 2, b / 2, h / 2]
    if theta > 0:
        tan_theta = math.tan((theta / 180) * math.pi)
        # if a*tan_theta/2 < h and a*tan_theta/2 <= (c-h): #梯形 1-正
        if (h > c / 2 and tan_theta <= (c - h) * 2 / a) or (h <= c / 2 and tan_theta < (h * 2) / a):
            print('梯形 1-正')
            record_cal[1] = record_cal[1] + 1
            mass_center_rect = [a / 2, b / 2, h / 2 - a * tan_theta / 4]
            mass_center_tria = [a / 3, b / 2, h - a * tan_theta / 6]
            m_rect = (h - a * tan_theta / 2) * a
            m_tria = a * a * tan_theta / 2
            mass_center_sum = [0, 0, 0]
            for i in range(3):
                mass_center_sum[i] = mass_center_rect[i] * m_rect + mass_center_tria[i] * m_tria
            return [k / (m_rect + m_tria) for k in mass_center_sum]
        if h <= c / 2 and (h * 2) / a <= tan_theta <= pow(c, 2) / (2 * a * h):
            # 三角形 1-正
            print('三角形 1-正')
            record_cal[2] = record_cal[2] + 1
            mass_center_tri = [pow(2 * a * h / tan_theta, 0.5) / 3, b / 2, pow(2 * a * h * tan_theta, 0.5) / 3]
            return mass_center_tri
        if h > c / 2 and (c - h) * 2 / a < tan_theta < pow(c, 2) / (2 * a * (c - h)):
            # 五边形 1-正
            print('五边形 1-正')
            record_cal[3] = record_cal[3] + 1
            x = a - pow(2 * a * (c - h) / tan_theta, 0.5)
            mass_center_rect1 = [x / 2, b / 2, c / 2]
            m_rect1 = x * c
            mass_center_rect2 = [x / 2 + a / 2, b / 2, (c - (a - x) * tan_theta) / 2]
            m_rect2 = (a - x) * (c - (a - x) * tan_theta)
            mass_center_tria = [(a + 2 * x) / 3, b / 2, c - 2 * (a - x) * tan_theta / 3]
            m_tria = pow(a - x, 2) * tan_theta / 2
            mass_center_sum = [0, 0, 0]
            for i in range(3):
                mass_center_sum[i] = mass_center_rect1[i] * m_rect1 + mass_center_rect2[i] * m_rect2 + mass_center_tria[
                    i] * m_tria
            return [k / (m_rect1 + m_rect2 + m_tria) for k in mass_center_sum]
        if (h <= c / 2 and tan_theta > pow(c, 2) / (2 * a * h)) or (
                h > c / 2 and tan_theta >= pow(c, 2) / (2 * a * (c - h))):
            print('梯形 2-正')
            record_cal[4] = record_cal[4] + 1
            # mass_center_rect = [a*h/2*c-c/4*tan_theta, b/2, c/2]
            x = a * h / c - c / (2 * tan_theta)
            mass_center_rect = [x / 2, b / 2, c / 2]
            m_rect = a * h - pow(c, 2) / (2 * tan_theta)
            mass_center_tria = [x + c / (3 * tan_theta), b / 2, c / 3]
            m_tria = pow(c, 2) / (2 * tan_theta)
            # print(str(m_rect + m_tria) + ' ' + str(a * h))
            mass_center_sum = [0, 0, 0]
            for i in range(3):
                mass_center_sum[i] = mass_center_rect[i] * m_rect + mass_center_tria[i] * m_tria
        return [k / (m_rect + m_tria) for k in mass_center_sum]
    # return [a / 2, b / 2, h / 2]
    if theta < 0:
        theta = abs(theta)
        tan_theta = math.tan(((theta / 180) * math.pi))
        if (h > c / 2 and tan_theta <= (c - h) * 2 / a) or (h <= c / 2 and tan_theta < (h * 2) / a):
            # if a * tan_theta / 2 < h and a * tan_theta / 2 <= (c - h):
            print('梯形 1-负')
            record_cal[5] = record_cal[5] + 1
            mass_center_rect = [a / 2, b / 2, h / 2 - a * tan_theta / 4]
            mass_center_tria = [2 * a / 3, b / 2, h - a * tan_theta / 6]
            m_rect = (h - a * tan_theta / 2) * a
            m_tria = a * a * tan_theta / 2
            mass_center_sum = [0, 0, 0]
            for i in range(3):
                mass_center_sum[i] = mass_center_rect[i] * m_rect + mass_center_tria[i] * m_tria
            return [k / (m_rect + m_tria) for k in mass_center_sum]
        if h <= c / 2 and (h * 2) / a <= tan_theta <= pow(c, 2) / (2 * a * h):
            print('三角形 1-负')
            record_cal[6] = record_cal[6] + 1
            mass_center_tri = [a - (pow(2 * a * h / tan_theta, 0.5) / 3), b / 2,
                               pow(2 * a * h * tan_theta, 0.5) / 3]
            return mass_center_tri
        if h > c / 2 and (c - h) * 2 / a < tan_theta < pow(c, 2) / (2 * a * (c - h)):
            print('五边形 1-负')
            record_cal[7] = record_cal[7] + 1
            x = a - pow(2 * a * (c - h) / tan_theta, 0.5)
            mass_center_rect1 = [a - x / 2, b / 2, c / 2]
            m_rect1 = x * c
            mass_center_rect2 = [a / 2 - x / 2, b / 2, (c - (a - x) * tan_theta) / 2]
            m_rect2 = (a - x) * (c - (a - x) * tan_theta)
            mass_center_tria = [(2 * a - 2 * x) / 3, b / 2, c - 2 * (a - x) * tan_theta / 3]
            m_tria = pow(a - x, 2) * tan_theta / 2
            # print(str(m_rect1 + m_rect2 + m_tria) + ' ' + str(a * h))
            mass_center_sum = [0, 0, 0]
            for i in range(3):
                mass_center_sum[i] = mass_center_rect1[i] * m_rect1 + mass_center_rect2[i] * m_rect2 + mass_center_tria[
                    i] * m_tria
            return [k / (m_rect1 + m_rect2 + m_tria) for k in mass_center_sum]
        # if (h<=c/2 and a*tan_theta/2>=h and 2*tan_theta*a*h>pow(c,2)) or (h>c/2 and (h+a*tan_theta/2) >= c and tan_theta*2*a*(c-h)>=pow(c,2)): #梯形
        if (h <= c / 2 and tan_theta > pow(c, 2) / (2 * a * h)) or (
                h > c / 2 and tan_theta >= pow(c, 2) / (2 * a * (c - h))):
            print('梯形 2-负')
            record_cal[8] = record_cal[8] + 1
            mass_center_rect = [a - a * h / (2 * c) + c / (4 * tan_theta), b / 2, c / 2]
            m_rect = a * h - pow(c, 2) / (2 * tan_theta)
            mass_center_tria = [a - a * h / c + c / (6 * tan_theta), b / 2, c / 3]
            m_tria = pow(c, 2) / (2 * tan_theta)
            # print(str(m_rect + m_tria) + ' ' + str(a * h))
            mass_center_sum = [0, 0, 0]
            for i in range(3):
                mass_center_sum[i] = mass_center_rect[i] * m_rect + mass_center_tria[i] * m_tria
            return [k / (m_rect + m_tria) for k in mass_center_sum]
        # return [a / 2, b / 2, h / 2]


def calMassCenters(weight_vs, theta):
    massCenters = []
    for i in range(6):
        weight_v = weight_vs[i + 1]  # kg/s 质量变化速度
        delta_m = weight_v * 1
        m_current = box_ms[i] - delta_m
        box_ms[i] = m_current
        v_current = m_current / ru
        box_vs[i] = v_current
        box_s = v_current / box_abcs[i][1]  # 当前的油体侧面积
        h = box_s / box_abcs[i][0]  # 如果 theta=0，计算出的油面高度
        print('h:' + str(h))
        print('a:' + str(box_abcs[i][0]))
        print('c:' + str(box_abcs[i][2]))
        massCenter = calMassCenterOfSingleBox(h, theta, box_abcs[i][0], box_abcs[i][1], box_abcs[i][2])
        print(massCenter)
        box_xyz_display = box_xyz0s[i]
        for p in range(3):
            massCenter[p] = massCenter[p] + box_xyz0s[i][p]  # 将坐标系转换到以飞行器为原点的坐标系
        box_mass_centers[i].append(massCenter)
        massCenters.append(massCenter)
    return massCenters


weight_data = xlrd.open_workbook('油箱供油曲线.xlsx')
weight_table = weight_data.sheets()[0]
theta_data = xlrd.open_workbook('飞行器俯仰角.xlsx')
theta_table = theta_data.sheets()[0]  # 7200 条数据
# 创建一个 workbook 设置编码
result_book = xlwt.Workbook(encoding='utf-8')
# 创建一个 worksheet
result_sheet = result_book.add_sheet('mass_center')
result_sheet.write(0, 0, label='t/s')
result_sheet.write(0, 1, label='x')
result_sheet.write(0, 2, label='y')
result_sheet.write(0, 3, label='z')

for i in range(weight_table.nrows - 1):
    weight_vs = weight_table.row_values(i + 1)
    weight_vs[2] = weight_vs[2] - weight_vs[1]  # 油箱 1 输送给油箱 2
    weight_vs[5] = weight_vs[5] - weight_vs[6]  # 油箱 6 输送给油箱 5
    theta = theta_table.row_values(i + 1)[1]
    print('index:' + str(i + 1))
    mass_centers = calMassCenters(weight_vs, theta)
    # print(box_ms)
    sum_m = 3000  # 还要加飞行器的质心
    sum_mass_center = [0, 0, 0]  # *sum_m
    for k in range(6):
        mass_center = mass_centers[k]
        # print(mass_center)
        m = box_ms[k]
        sum_m = sum_m + m
        sum_mass_center = [d + m * n for d, n in zip(sum_mass_center, mass_center)]
    mass_center_planet = [t / sum_m for t in sum_mass_center]
    result_sheet.write(i + 1, 0, label=str(i + 1))
    result_sheet.write(i + 1, 1, label=str(mass_center_planet[0]))
    result_sheet.write(i + 1, 2, label=str(mass_center_planet[1]))
    result_sheet.write(i + 1, 3, label=str(mass_center_planet[2]))
result_book.save('mass_center_result.xls')
for p in range(6):
    box_mass_center = box_mass_centers[p]
    result_book = xlwt.Workbook(encoding='utf-8')
    # 创建一个 worksheet
    result_sheet = result_book.add_sheet('mass_center')
    result_sheet.write(0, 0, label='t/s')
    result_sheet.write(0, 1, label='x')
    result_sheet.write(0, 2, label='y')
    result_sheet.write(0, 3, label='z')
    for i in range(len(box_mass_center) - 1):
        mass_center = box_mass_center[i]
        result_sheet.write(i + 1, 0, label=str(i + 1))
        result_sheet.write(i + 1, 1, label=str(mass_center[0]))
        result_sheet.write(i + 1, 2, label=str(mass_center[1]))
        result_sheet.write(i + 1, 3, label=str(mass_center[2]))
    result_book.save('mass_center_box_' + str(p) + '.xls')
