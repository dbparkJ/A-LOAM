import os
from rosbag import Bag
from tqdm import tqdm

input_folder = '/media/geonslam/SelfDriving_DATA/2024-03-04/2024-03-04-14-13-53'  # 백 파일이 저장된 폴더 경로
output_folder = '/media/geonslam/SelfDriving_DATA/2024-03-04/outputfolder3'  # 변환된 백 파일을 저장할 폴더 경로

# 만약 output_folder가 존재하지 않으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# input_folder 내의 모든 백 파일을 가져옴
bag_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.bag')])

for bag_file in bag_files:
    input_path = os.path.join(input_folder, bag_file)

    # 출력 백 파일의 이름을 변경하려면 여기서 수정
    output_file_name = 'prefix_' + bag_file  # 원하는 이름 패턴으로 변경

    output_path = os.path.join(output_folder, output_file_name)

    print(f"변환 중: {bag_file} -> {output_file_name}")

    with Bag(output_path, 'w') as Y:
        bag = Bag(input_path)
        for topic, msg, t in tqdm(bag.read_messages(), desc=f"변환 중: {bag_file}"):
            if topic == '/lidar0/velodyne_points':
                Y.write('/velodyne_points', msg, t)
            else:
                Y.write(topic, msg, t)

    print(f"{bag_file} 변환이 완료되었습니다.")

print("모든 백 파일 변환 완료")

