import asyncio
import threading
import multiprocessing
import time

async def download_sheet(file_name):
    print(f"[Async] เริ่มดาวน์โหลด: {file_name}")
    await asyncio.sleep(2)
    print(f"[Async] โหลดเสร็จแล้ว: {file_name}")

async def run_async():
    print("--- 1. เริ่มทดสอบ Asyncio ---")
    tasks = [
        download_sheet("ชีทคณิตศาสตร์.pdf"),
        download_sheet("ชีทโปรแกรมมิ่ง.pdf"),
        download_sheet("ชีทฟิสิกส์.pdf")
    ]
    await asyncio.gather(*tasks)
    print("--------------------------\n")

def print_document(doc_name):
    print(f"[Thread] กำลังสั่งปรินต์: {doc_name}")
    time.sleep(2)  # จำลองเครื่องปรินต์ทำงาน 2 วินาที
    print(f"[Thread] ปรินต์เสร็จแล้ว: {doc_name}")

def run_threads():
    print("--- 2. เริ่มทดสอบ Threading ---")
    documents = ["รายงานบทที่ 1", "รายงานบทที่ 2", "รายงานบทที่ 3"]
    threads = []
    
    for doc in documents:
        t = threading.Thread(target=print_document, args=(doc,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
    print("--------------------------\n")


def calculate_heavy_math(job_id):
    print(f"[Process] เริ่มคำนวณงานที่ {job_id}...")
    total = sum(i * i for i in range(5_000_000))
    print(f"[Process] คำนวณงานที่ {job_id} เสร็จสิ้น!")
    return total

def run_process_pool():
    print("--- 3. เริ่มทดสอบ Process Pool ---")
    jobs = [1, 2, 3]
    
    with multiprocessing.Pool(processes=3) as pool:
        pool.map(calculate_heavy_math, jobs)
    print("--------------------------\n")

if __name__ == "__main__":
    # รันทั้ง 3 แบบเรียงตามลำดับ
    asyncio.run(run_async())
    run_threads()
    run_process_pool()