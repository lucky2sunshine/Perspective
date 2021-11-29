import os.path
from time import sleep
from googleapiclient import discovery
import json

class Perspectiveapi:

  @staticmethod
  def check(text, method = 'TOXICITY'):
    """
    检测单条评论的毒性
    :param1: text 要检测的文本
    :return: JSON 检测结果
    """
    API_KEY = 'XXXXXXXXXXXXX'

    client = discovery.build(
      "commentanalyzer",
      "v1alpha1",
      developerKey=API_KEY,
      discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
      static_discovery=False,
    )

    analyze_request = {
      'comment': {'text': text},
      'requestedAttributes': {method : {}},
    }

    response = client.comments().analyze(body=analyze_request).execute()
    return json.dumps(response, indent=2)

  @staticmethod
  def check_from_file(filePath, method = 'TOXICITY'):
    """
    在文件中读取评论进行毒性检测,并将结果写入文件
    :param filePath: 文件路径
    :param method: 检测方式
    """
    result = {}
    f = open(filePath)
    lines = f.readlines()
    save_file_name = os.path.basename(filePath).split('.')[0]
    with open('./' + save_file_name + '_result.csv', 'w', encoding='utf-8') as f:
      for line in lines:
        line = line.strip('\n')
        try:
          score = json.loads(Perspectiveapi.check(line, method))
        except Exception as e:
          sleep(2)
          print(e)
          continue
        score = score['attributeScores'][method]['summaryScore']['value']
        result[line] = score
        print(line, score)
        sleep(2)
        f.write(line + '\t' + str(score) + '\n')

  @staticmethod
  def check_from_list(comments, method='TOXICITY'):
    """
    在文件中读取评论进行毒性检测,并将结果写入文件
    :param comments:  list 评论
    :param method: 检测方式
    """
    result = {}
    save_file_name = 'litaowan'
    with open('./' + save_file_name + '_result.csv', 'w', encoding='utf-8') as f:
      for comment in comments:
        comment = comment.strip('\n')
        if comment == '':
          continue
        try:
          score = json.loads(Perspectiveapi.check(comment, method))
        except:
          sleep(2)
          continue
        score = score['attributeScores'][method]['summaryScore']['value']
        result[comment] = score
        print(comment, score)
        sleep(2)
        f.write(comment + '\t' + str(score) + '\n')

if __name__ == '__main__':
  # Perspectiveapi.check_from_file('./sentences.txt')
  # print(Perspectiveapi.check_from_file('./sentence2.txt'))
  # print(Perspectiveapi.check_from_file('./sentences_random.txt'))
  # print(Perspectiveapi.check("FUcK!!!"))
  # Perspectiveapi.check_from_file('./confusion1.txt')
  # Perspectiveapi.check_from_file('./confusion2.txt')
  # Perspectiveapi.check_from_file('./confusion3.txt')
  Perspectiveapi.check_from_file('./confusion4.txt')

  pass

