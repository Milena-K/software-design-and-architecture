import Head from "next/head";
import Menu from "./Menu";
import MainPage from "./MainPage";
import Layout from "./Layout";

export default function Home() {
  return (
    <>
      <Head>
        <title>Create T3 App</title>
        <meta name="description" content="Generated by create-t3-app" />
      </Head>
      <main>
        <Layout>
          <MainPage/>
        </Layout>
      </main>
    </>
  );
}
