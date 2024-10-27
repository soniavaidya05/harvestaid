import Image from "next/image";
import Link from "next/link";
import { Chewy } from "next/font/google";

const chewyFont = Chewy({ subsets: ["latin"], weight: "400" });

export default function Home() {
  return (
    <div
      style={{ backgroundColor: "rgb(245, 244, 227)" }}
      className="flex h-screen flex-col"
    >
      <div className="flex justify-center items-center relative bg-[#b2c0b0] drop-shadow-md">
        <Image
          src="/HarvestAidText.png"
          alt="Harvest Aid Text"
          width={2300}
          height={500}
          className="my-auto objection-contain"
        />
      </div>
      <div className="flex justify-center h-2/3">
        <Link
          className={`mx-auto my-auto px-5 py-2 text-3xl text-white bg-[#b2c0b0] border-b-4 border-[#8b9c8d] rounded transition ease-in-out transform hover:translate-y-1 hover:border-0 ${chewyFont.className}`}
          href="/login"
        >
          Get Started
        </Link>
      </div>
    </div>
  );
}
