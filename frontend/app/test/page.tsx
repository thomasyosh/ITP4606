export default async function Page() {
  const data = await fetch('http://backend:8000/')
  const posts = await data.json()
  return (
    <ul>
      {posts.map((post : any) => (
        <li key={post.pk_id}>{post.name}</li>
      ))}
    </ul>
  )
}