import pandas as pd

def score():
    data = {'이름': [], '점수': []}

    while len(data['이름']) < 5:
        name = input(f"학생 {len(data['이름']) + 1} ")
        if name == '끝':
            break
        try:
            score = float(input('점수: '))
        except ValueError:
            print('점수 입력')
            continue
        data['이름'].append(name)
        data['점수'].append(score)

    df = pd.DataFrame(data)
    if df.empty:
        print('입력된 정보가 없음')
        return
    
    age = df['점수'].mean()
    max_score = df['점수'].max()
    top_studen = df[df['점수'] == max_score]['이름'].tolist()

    print(f"\n전체 학생 수: {len(df)}명")
    print(f"평균 점수: {age:.2f}")
    print(f"최고 점수: {max_score}점")
    print(f"최고 점수를 맞은 학생: {','.join(top_studen)}")

if __name__ == "__main__":
    score()
